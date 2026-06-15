# vllm-project/vllm#5490: 当调用接口，不传system时，输出卡主了，输出全是！！！！！

| 字段 | 值 |
| --- | --- |
| Issue | [#5490](https://github.com/vllm-project/vllm/issues/5490) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> 当调用接口，不传system时，输出卡主了，输出全是！！！！！

### Issue 正文摘录

### Your current environment 启动方式：python -m vllm.entrypoints.openai.api_server --model /opt/llm_models/Qwen1.5-32B-Chat-GPTQ-Int4 --quantization gptq --max-model-len 16384 --port 8888 --gpu-memory-utilization 0.7 --tensor-parallel-size 2 --host 0.0.0.0 --served-model-name Qwen1.5-32B-Chat-GPTQ-Int4 --trust-remote-code --enforce-eager --engine-use-ray --worker-use-ray 两张A10，vllm 0.4.0.post1 - vllm 0.5.0 版本 都有此问题 ### 🐛 Describe the bug **当调用接口，不传system时，输出卡主了，用户日志输出全是！！！！！** vllm输出日志如下： INFO 06-13 07:32:54 async_llm_engine.py:561] Received request cmpl-ce462c327b014a60936becb6d1bb06ab: prompt: ' system\nYou are a helpful assistant. \n user\n\n你好啊，你能干什么，11111111111111111111 \n assistant\n', params: SamplingParams(n=1, best_of=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.1, top_p=1.0, top_k=-1, min_p=0.0, seed=None, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=16339, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None), prompt_token_ids: [151644, 8...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: rypoints.openai.api_server --model /opt/llm_models/Qwen1.5-32B-Chat-GPTQ-Int4 --quantization gptq --max-model-len 16384 --port 8888 --gpu-memory-utilization 0.7 --tensor-parallel-size 2 --host 0.0.0.0 --served-model-nam...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: current environment 启动方式：python -m vllm.entrypoints.openai.api_server --model /opt/llm_models/Qwen1.5-32B-Chat-GPTQ-Int4 --quantization gptq --max-model-len 16384 --port 8888 --gpu-memory-utilization 0.7 --tensor-parall...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 当调用接口，不传system时，输出卡主了，输出全是！！！！！ bug;stale ### Your current environment 启动方式：python -m vllm.entrypoints.openai.api_server --model /opt/llm_models/Qwen1.5-32B-Chat-GPTQ-Int4 --quantization gptq --max-model-len 16384 --por...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: tokens=16339, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None), prompt_token_ids: [151644, 8948, 198, 2610, 525, 264, 10950, 1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: , temperature=0.1, top_p=1.0, top_k=-1, min_p=0.0, seed=None, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
