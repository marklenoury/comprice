import Dependencies._

lazy val root = (project in file(".")).
  settings(
    inThisBuild(List(
      organization := "za.co.comprice",
      scalaVersion := "2.12.5",
      version      := "0.1.0-SNAPSHOT"
    )),
    name := "httpserver",
    libraryDependencies ++= Seq(
      scalaTest % Test,
      "io.netty" % "netty-all" % "4.1.23.Final"
    ),
    mainClass in assembly := Some("za.co.comprice.HttpServer")
  )
