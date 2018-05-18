package za.co.comprice

import java.net.InetSocketAddress

import io.netty.bootstrap.ServerBootstrap
import io.netty.channel.group.{ChannelGroup, DefaultChannelGroup}
import io.netty.channel.{Channel, ChannelInitializer}
import io.netty.channel.nio.NioEventLoopGroup
import io.netty.channel.socket.nio.NioServerSocketChannel
import io.netty.handler.codec.http.{HttpObjectAggregator, HttpServerCodec}
import io.netty.handler.stream.ChunkedWriteHandler
import io.netty.util.concurrent.ImmediateEventExecutor

class HttpServerChannelInitializer(httpRequestHandler: HttpRequestHandler,
                                   group: ChannelGroup
                                  ) extends ChannelInitializer[Channel] {
  override def initChannel(ch: Channel): Unit = {
    val pipeline = ch.pipeline()
    pipeline.addLast(new HttpServerCodec)
    pipeline.addLast(new ChunkedWriteHandler)
    pipeline.addLast(new HttpObjectAggregator(64 * 1024))
    pipeline.addLast(httpRequestHandler)
  }

}

class HttpServer(port: Int, baseLocation: String) {
  def start = {
    val httpRequestHandler = HttpRequestHandler(baseLocation)
    val channelGroup = new DefaultChannelGroup(ImmediateEventExecutor.INSTANCE)
    val eventLoopGroup = new NioEventLoopGroup()
    try {
      val serverBootstrap = new ServerBootstrap()
      serverBootstrap
        .group(eventLoopGroup)
        .channel(classOf[NioServerSocketChannel])
        .localAddress(new InetSocketAddress(port))
        .childHandler(new HttpServerChannelInitializer(httpRequestHandler, channelGroup))

      val channelFuture = serverBootstrap.bind().sync()
      channelFuture.channel().closeFuture().sync()
    } catch {
      case ex: Exception => {
        System.err.println(ex.toString)
      }
    } finally {
      eventLoopGroup.shutdownGracefully().sync()
    }
  }
}

object HttpServer {
  def main(args: Array[String]): Unit = {
    if (args.length != 2) {
      System.err.println(s"Usage: ${HttpServer.getClass.getSimpleName} <port> <baseLocation>")
      return
    }

    val httpServer = new HttpServer(args(0).toInt, args(1))
    httpServer.start
  }
}
