# vllm-project/vllm#29847: [Feature]: enable FastAPI documention (`/docs`) for air-gaped host

| 字段 | 值 |
| --- | --- |
| Issue | [#29847](https://github.com/vllm-project/vllm/issues/29847) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: enable FastAPI documention (`/docs`) for air-gaped host

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When used on a air-gaped system, FastAPI documentation route (`/docs`) is not accessible because it requires pulling static content from internet. This route is very useful because it is both a documentation and a simple way to send requests to the server, easing a lot when integrating vllm to a system. One simple way to enable this route is to use the [fastapi_offline](https://github.com/turettn/fastapi_offline) package and edit the way we call the app object : ``` from fastapi import FastAPI app = FastAPI() ``` by ``` from fastapi_offline import FastAPIOffline app = FastAPIOffline() ``` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ine) package and edit the way we call the app object : ``` from fastapi import FastAPI app = FastAPI() ``` by ``` from fastapi_offline import FastAPIOffline app = FastAPIOffline() ``` ### Alternatives _No response_ ###...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: eature]: enable FastAPI documention (`/docs`) for air-gaped host feature request ### 🚀 The feature, motivation and pitch When used on a air-gaped system, FastAPI documentation route (`/docs`) is not accessible because i...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
