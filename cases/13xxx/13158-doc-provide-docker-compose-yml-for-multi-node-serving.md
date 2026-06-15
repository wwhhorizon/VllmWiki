# vllm-project/vllm#13158: [Doc]: provide docker-compose.yml for multi-node serving

| 字段 | 值 |
| --- | --- |
| Issue | [#13158](https://github.com/vllm-project/vllm/issues/13158) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: provide docker-compose.yml for multi-node serving

### Issue 正文摘录

### 📚 The doc issue now deploy deepseek-r1 is very difficult for multi-node serving, the params of serving deepseek-r1 is more and more, run _cluster.sh should has a lot of params. after docker stop and start , it should be also set a lot of params again. if has a docker-compose.yml , is only set the params once, then can use `docker compose up -d` to start it, no should think params how to set after once. ### Suggest a potential alternative/fix provide docker-compose.yml example for multi-node serving， include ray , vllm node1 docker-compose.yml ``` services: redis: ... ray: ... vllm: ... ``` node2 docker-compose.yml ``` services: ray: ... vllm: ... ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Doc]: provide docker-compose.yml for multi-node serving documentation;stale ### 📚 The doc issue now deploy deepseek-r1 is very difficult for multi-node serving, the params of serving deepseek-r1 is more and more, run _...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Doc]: provide docker-compose.yml for multi-node serving documentation;stale ### 📚 The doc issue now deploy deepseek-r1 is very difficult for multi-node serving, the params of serving deepseek-r1 is more and more, run _...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
