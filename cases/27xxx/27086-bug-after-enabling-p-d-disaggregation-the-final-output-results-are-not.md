# vllm-project/vllm#27086: [Bug]: After enabling P-D Disaggregation, the final output results are not entirely identical.

| 字段 | 值 |
| --- | --- |
| Issue | [#27086](https://github.com/vllm-project/vllm/issues/27086) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: After enabling P-D Disaggregation, the final output results are not entirely identical.

### Issue 正文摘录

### Your current environment vllm VERSION： 0.10.1 ### 🐛 Describe the bug When I fixed the random seed and ensured all environment variables were consistent, I noticed that launching PD separation with the same configuration produced inconsistent final outputs. This phenomenon may require multiple attempts to fully manifest. I have a question: Is this behavior normal? (under temperature=0 conditions) vllm startup script （D），The startup process for P nodes is almost identical, except for the use of “kv_producer”. ``` VLLM_CFG=( --trust-remote-code --data-parallel-size 1 --tensor-parallel-size 8 --no-enable-prefix-caching --no-enable-chunked-prefill --kv-transfer-config '{"kv_connector":"NixlConnector","kv_role":"kv_consumer"}' ) ``` When requested, temperature=0 ``` curl -X POST -s http://${HOST_PORT}/v1/completions \ -H "Content-Type: application/json" \ -d '{ "model": "base_model", "prompt": "xxxx", # The prompt is identical for every request, and this prompt will also appear. "max_tokens": 1000, "temperature": 0, "stream": true }' printf "\n" ``` My question is: Does the PD also have a probability of producing non-identical outputs at every step when temperature=0? If this is a n...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Disaggregation, the final output results are not entirely identical. bug;stale ### Your current environment vllm VERSION： 0.10.1 ### 🐛 Describe the bug When I fixed the random seed and ensured all environment variables...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: are not entirely identical. bug;stale ### Your current environment vllm VERSION： 0.10.1 ### 🐛 Describe the bug When I fixed the random seed and ensured all environment variables were consistent, I noticed that launching...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: es were consistent, I noticed that launching PD separation with the same configuration produced inconsistent final outputs. This phenomenon may require multiple attempts to fully manifest. I have a question: Is this beh...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ou. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
