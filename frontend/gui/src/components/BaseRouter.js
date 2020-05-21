import React from "react";
import { Route } from "react-router-dom";
import ArrayList from "./ArrayList";
import ArticleDetail from "./ArticleDetail";
import login from "./login";
import signup from "./signup";

const BaseRouter = () => {
  return (
    <div>
      <Route exact path="/" component={ArrayList} />
      <Route exact path="/:articleID" component={ArticleDetail} />
      <Route exact path="/article/registration" component={login} />
      <Route exact path="/article/signup/" component={signup} />
    </div>
  );
};

export default BaseRouter;
