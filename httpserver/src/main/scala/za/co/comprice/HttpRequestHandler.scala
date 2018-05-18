package za.co.comprice

import io.netty.channel.ChannelHandler.Sharable
import io.netty.channel.{ChannelFutureListener, ChannelHandlerContext, SimpleChannelInboundHandler}
import io.netty.handler.codec.http._
import io.netty.handler.stream.ChunkedNioFile

@Sharable
class HttpRequestHandler extends SimpleChannelInboundHandler[FullHttpRequest] {
 private var indexFile: java.io.File = null
  private var chartJSFile: java.io.File = null


  def getIndexHtml(ctx: ChannelHandlerContext, msg: FullHttpRequest): Unit = {
    val response = new DefaultHttpResponse(
      msg.protocolVersion(),
      HttpResponseStatus.OK
    )

    response.headers().set(
      HttpHeaderNames.CONTENT_TYPE, "text/html; charset=UTF-8"
    )

    ctx.write(response)
    ctx.write(new ChunkedNioFile(indexFile))
    val channelFuture = ctx.writeAndFlush(LastHttpContent.EMPTY_LAST_CONTENT)
    channelFuture.addListener(ChannelFutureListener.CLOSE)
  }

  def getChartJS(ctx: ChannelHandlerContext, msg: FullHttpRequest): Unit = {
    println("getChartJS")
    val response = new DefaultHttpResponse(
      msg.protocolVersion(),
      HttpResponseStatus.OK
    )

    response.headers().set(
      HttpHeaderNames.CONTENT_TYPE, "application/javascript; charset=UTF-8"
    )

    ctx.write(response)
    ctx.write(new ChunkedNioFile(chartJSFile))
    val channelFuture = ctx.writeAndFlush(LastHttpContent.EMPTY_LAST_CONTENT)
    channelFuture.addListener(ChannelFutureListener.CLOSE)
  }

  def handle404(ctx: ChannelHandlerContext, msg: FullHttpRequest): Unit = {
    println("handle404")
    val response = new DefaultHttpResponse(
      msg.protocolVersion(),
      HttpResponseStatus.NOT_FOUND
    )

    val channelFuture = ctx.writeAndFlush(response)
    channelFuture.addListener(ChannelFutureListener.CLOSE)
  }

  override def channelRead0(ctx: ChannelHandlerContext, msg: FullHttpRequest): Unit = {
    println(s"Received request for URI: ${msg.uri()}")
    msg.uri() match {
      case "/index.html" => getIndexHtml(ctx, msg)
      case "/Chart.bundle.min.js" => getChartJS(ctx, msg)
      case _ => handle404(ctx, msg)
    }
  }

  override def exceptionCaught(ctx: ChannelHandlerContext, cause: Throwable): Unit = {
    cause.printStackTrace()
    ctx.close()
  }
}


object HttpRequestHandler {
  def apply(baseLocation: String) = {
    val handler = new HttpRequestHandler()
    val indexFilePath = s"$baseLocation/index.html"
    handler.indexFile = new java.io.File(indexFilePath)
    val chartJSFilePath = s"$baseLocation/Chart.bundle.min.js"
    handler.chartJSFile = new java.io.File(chartJSFilePath)
    handler
  }
}
