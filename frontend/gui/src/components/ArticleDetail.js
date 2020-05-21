import React, { Component } from "react";
import { Card, Button, Form } from "antd";
import axios from "axios";
import CustomForm from "./Form";
import { withRouter } from "react-router-dom";
class ArticleDetail extends Component {
  constructor(props) {
    super(props);
    this.state = {
      articles: []
    };
  }

  componentDidMount() {
    const articleid = this.props.match.params.articleID;
    axios.get(`http://127.0.0.1:8000/api/${articleid}`).then(res => {
      this.setState({ articles: res.data });
      console.log(res.data);
    });
  }

  handleDelete = event => {
    console.log("delete");
    const articleid = this.props.match.params.articleID;
    axios.delete(`http://127.0.0.1:8000/api/${articleid}/delete`);
    this.props.histroy.push("/");
    this.forceUpdate();
  };

  render() {
    return (
      <div>
        <Card title={this.state.articles.title}>
          <p>{this.state.articles.content}</p>
        </Card>
        <br />
        <CustomForm
          articleID={this.props.match.params.articleID}
          requestType="put"
          btnText="Update"
        />
        <Form onSubmit={this.handleDelete}>
          <Button type="danger" htmlType="submit">
            Delete
          </Button>
        </Form>
      </div>
    );
  }
}

export default withRouter(ArticleDetail);
