# vllm-project/vllm#11317: [Performance]: vllm0.6.5加载GLM4-9B-Chat，动态加载lora，输入长文本时推理性能下降较多

| 字段 | 值 |
| --- | --- |
| Issue | [#11317](https://github.com/vllm-project/vllm/issues/11317) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: vllm0.6.5加载GLM4-9B-Chat，动态加载lora，输入长文本时推理性能下降较多

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression ### A800，单卡处理单条请求 1. **vllm0.6.5不加载lora** （1）启动： CUDA_VISIBLE_DEVICES=7 python -m vllm.entrypoints.openai.api_server --model /Work/....../glm-4-9b-chat/ --trust-remote-code （2）请求： response = client.chat.completions.create( model='/Work/....../glm-4-9b-chat/', messages=messages, n=1, temperature=0, extra_body={"stop_token_ids": [151329, 151336, 151338]}, max_tokens=2048, stream=True) 2. **vllm0.6.5动态加载lora** 【lora模型使用llama_factory框架训练】 （1）启动： CUDA_VISIBLE_DEVICES=7 python -m vllm.entrypoints.openai.api_server --model /Work/....../glm-4-9b-chat/ --enable-lora --max-loras 10 --lora-modules summary=/Work/....../sft_1218/ --trust-remote-code --max-lora-rank 64 （2）请求： response = client.chat.completions.create( model='summary', messages=messages, n=1, temperature=0, extra_body={"stop_token_ids": [151329, 151336, 151338]}, max_tokens=2048, stream=True) **测试messages中输入不同长度文本时，不同情况下的推理速度：** ![d2dccaa39734cc6f41449b48aad6a65](https://github.com/user-attachments/assets/c28cbcfb-447b-49b4-972c-00569e52730f) 发现加载lora后，输入文本较长时，推理速度相比于不加载lora下降较多，输入文本较短时下降不多 请问是什么原因造成的，我应该如何解决？谢谢~ ### Misc discussion on perform...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: performance regression ### A800，单卡处理单条请求 1. **vllm0.6.5不加载lora** （1）启动： CUDA_VISIBLE_DEVICES=7 python -m vllm.entrypoints.openai.api_server --model /Work/....../glm-4-9b-chat/ --trust-remote-code （2）请求： response = clien...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 动： CUDA_VISIBLE_DEVICES=7 python -m vllm.entrypoints.openai.api_server --model /Work/....../glm-4-9b-chat/ --trust-remote-code （2）请求： response = client.chat.completions.create( model='/Work/....../glm-4-9b-chat/', messa...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: roposal to improve performance _No response_ ### Report of performance regression ### A800，单卡处理单条请求 1. **vllm0.6.5不加载lora** （1）启动： CUDA_VISIBLE_DEVICES=7 python -m vllm.entrypoints.openai.api_server --model /Work/.........
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: erformance]: vllm0.6.5加载GLM4-9B-Chat，动态加载lora，输入长文本时推理性能下降较多 performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression ### A800，单卡处理单条请求 1. **vllm0.6.5不加载lora** （1）启动： CUDA...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
