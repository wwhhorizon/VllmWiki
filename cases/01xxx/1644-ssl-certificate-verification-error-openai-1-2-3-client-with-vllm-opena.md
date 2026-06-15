# vllm-project/vllm#1644: SSL Certificate Verification Error Openai 1.2.3 client with vllm openai compatible api

| 字段 | 值 |
| --- | --- |
| Issue | [#1644](https://github.com/vllm-project/vllm/issues/1644) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> SSL Certificate Verification Error Openai 1.2.3 client with vllm openai compatible api

### Issue 正文摘录

**Description**: I am encountering an issue when attempting to use the official OpenAI client with the VLLM OpenAI-compatible API. Specifically, when trying to connect to the API using the official OpenAI client with versions greater than 1.0.0, I consistently receive the following error: ` httpcore.connection:starttls.failed exception=ConnectError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1124)'))` **Details**: Issue Type: Bug API Client: Official OpenAI client Error Version: OpenAI > 1.0.0 Error Message: httpcore.connection:starttls.failed exception=ConnectError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1124)')) **Additional Information:** - The error does not occur with OpenAI versions 1.0.0. - Connect to the VLLM OpenAI-compatible API. **Expected Behavior:** I expect the OpenAI API connection to work without SSL certificate verification errors, even with versions greater than 1.0.0. **Environment:** Operating System: MACOS Python Version:3.8.6 OpenAI Client Version: 1.2.3 **Note:** If you hav...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: escription**: I am encountering an issue when attempting to use the official OpenAI client with the VLLM OpenAI-compatible API. Specifically, when trying to connect to the API using the official OpenAI client with versi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: : unable to get local issuer certificate (_ssl.c:1124)')) **Additional Information:** - The error does not occur with OpenAI versions 1.0.0. - Connect to the VLLM OpenAI-compatible API. **Expected Behavior:** I expect t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
