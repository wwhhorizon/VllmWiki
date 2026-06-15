# vllm-project/vllm#25375: [Bug]: Issue downloading model from a local HF repository in Jfrog Artifactory

| 字段 | 值 |
| --- | --- |
| Issue | [#25375](https://github.com/vllm-project/vllm/issues/25375) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Issue downloading model from a local HF repository in Jfrog Artifactory

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm facing problems to deploy models directly from our private HuggingFace repository in Jfrog Artifactory, due to not take in account the CA certs that I installed inside the docker image. It gives me the following error: ` requests.exceptions.SSLError: (MaxRetryError("HTTPSConnectionPool(host='xxxxxxxxx', port=443): Max retries exceeded with url: /artifactory/api/huggingfacemlxxxxxx/api/models/xxxxx/xxxxx/tree/main?recursive=True&expand=False (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)')))"), '(Request ID: dd8e5b1c-3926-4835-a4aa-1c351be836eb)') ` I tried the following flags of Vllm: --ssl-ca-certs, --ssl-certfile I also tried to setup following environment variable: REQUEST_CA_BUNDLE all without making it work. Thanks you in advance. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: bug;stale ### Your current environment ### 🐛 Describe the bug I'm facing problems to deploy models directly from our private HuggingFace repository in Jfrog Artifactory, due to not take in account the CA certs that I in...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Issue downloading model from a local HF repository in Jfrog Artifactory bug;stale ### Your current environment ### 🐛 Describe the bug I'm facing problems to deploy models directly from our private HuggingFace rep...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ue downloading model from a local HF repository in Jfrog Artifactory bug;stale ### Your current environment ### 🐛 Describe the bug I'm facing problems to deploy models directly from our private HuggingFace repository in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ce. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ingfacemlxxxxxx/api/models/xxxxx/xxxxx/tree/main?recursive=True&expand=False (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certif...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
