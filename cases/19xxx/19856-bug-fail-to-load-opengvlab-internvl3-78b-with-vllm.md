# vllm-project/vllm#19856: [Bug]: fail to load OpenGVLab/InternVL3-78B with vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#19856](https://github.com/vllm-project/vllm/issues/19856) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: fail to load OpenGVLab/InternVL3-78B with vllm

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug failed to load OpenGVLab/InternVL3-78B model. use command: ``` python3.10 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8080 --model OpenGVLab/InternVL3-78B/ --tensor-parallel-size 8 --trust-remote-code ``` (VllmWorker rank=3 pid=16966) INFO 06-19 05:08:42 [topk_topp_sampler.py:44] Currently, FlashInfer top-p & top-k sampling sampler is disabled because FlashInfer>=v0.2.3 is not backward compatible. Falling back to the PyTorch-native implementation of top-p & top-k sampling. (VllmWorker rank=0 pid=16860) INFO 06-19 05:08:42 [topk_topp_sampler.py:44] Currently, FlashInfer top-p & top-k sampling sampler is disabled because FlashInfer>=v0.2.3 is not backward compatible. Falling back to the PyTorch-native implementation of top-p & top-k sampling. (VllmWorker rank=1 pid=16892) INFO 06-19 05:08:42 [topk_topp_sampler.py:44] Currently, FlashInfer top-p & top-k sampling sampler is disabled because FlashInfer>=v0.2.3 is not backward compatible. Falling back to the PyTorch-native implementation of top-p & top-k sampling. Loading safetensors checkpoint shards: 0% Completed | 0/31 [00:00 (VllmWorker rank=5 pid=17041) Traceback (...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: nk=3 pid=16966) INFO 06-19 05:08:42 [topk_topp_sampler.py:44] Currently, FlashInfer top-p & top-k sampling sampler is disabled because FlashInfer>=v0.2.3 is not backward compatible. Falling back to the PyTorch-native im...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: fail to load OpenGVLab/InternVL3-78B with vllm bug ### Your current environment ### 🐛 Describe the bug failed to load OpenGVLab/InternVL3-78B model. use command: ``` python3.10 -m vllm.entrypoints.openai.api_serv...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ust-remote-code ``` (VllmWorker rank=3 pid=16966) INFO 06-19 05:08:42 [topk_topp_sampler.py:44] Currently, FlashInfer top-p & top-k sampling sampler is disabled because FlashInfer>=v0.2.3 is not backward compatible. Fal...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: led ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
