# vllm-project/vllm#4520: [Bug]: Failing to find LoRA adapter for MultiLoRA Inference

| 字段 | 值 |
| --- | --- |
| Issue | [#4520](https://github.com/vllm-project/vllm/issues/4520) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Failing to find LoRA adapter for MultiLoRA Inference

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug I'm running the latest docker image and an openai style endpoint. My command is: ``` --model NousResearch/Meta-Llama-3-8B-Instruct --max-model-len 8192 --port 8000 --enable-lora --lora-modules forced-french=Trelis/Meta-Llama-3-8B-Instruct-forced-french-adapters --max-loras 1 --max-lora-rank 8 ``` I'm hitting the endpoint (on runpod) with: ``` curl https://y55xy7ozoxrn15-8000.proxy.runpod.net/v1/completions \ -H "Content-Type: application/json" \ -d '{ "model": "forced-french", "prompt": "Why did the chicken cross the road?", "max_tokens": 50, "temperature": 0 }' ``` The error is: ``` terminal: Internal Server Error logs: 2024-05-01T08:45:12.669025667Z ERROR 05-01 08:45:12 async_llm_engine.py:43] return func(*args, **kwargs) 2024-05-01T08:45:12.669029441Z ERROR 05-01 08:45:12 async_llm_engine.py:43] File "/usr/local/lib/python3.10/dist-packages/vllm/worker/worker.py", line 249, in execute_model 2024-05-01T08:45:12.669035014Z ERROR 05-01 08:45:12 async_llm_engine.py:43] output = self.model_runner.execute_model(seq_group_metadata_list, 2024-05-01T08:45:12.669038735Z ERROR 05-01 08:45...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: llm_engine.py:43] output = self.model_runner.execute_model(seq_group_metadata_list, 2024-05-01T08:45:12.669038735Z ERROR 05-01 08:45:12 async_llm_engine.py:43] File "/usr/local/lib/python3.10/dist-packages/torch/utils/_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: latest docker image and an openai style endpoint. My command is: ``` --model NousResearch/Meta-Llama-3-8B-Instruct --max-model-len 8192 --port 8000 --enable-lora --lora-modules forced-french=Trelis/Meta-Llama-3-8B-Instr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Failing to find LoRA adapter for MultiLoRA Inference bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug I'm running the latest docker image and an open...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: thon collect_env.py` ``` ### 🐛 Describe the bug I'm running the latest docker image and an openai style endpoint. My command is: ``` --model NousResearch/Meta-Llama-3-8B-Instruct --max-model-len 8192 --port 8000 --enabl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: image and an openai style endpoint. My command is: ``` --model NousResearch/Meta-Llama-3-8B-Instruct --max-model-len 8192 --port 8000 --enable-lora --lora-modules forced-french=Trelis/Meta-Llama-3-8B-Instruct-forced-fre...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
