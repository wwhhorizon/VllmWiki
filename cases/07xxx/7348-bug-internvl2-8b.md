# vllm-project/vllm#7348: [Bug]: internvl2-8b 提问无限循环回答

| 字段 | 值 |
| --- | --- |
| Issue | [#7348](https://github.com/vllm-project/vllm/issues/7348) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: internvl2-8b 提问无限循环回答

### Issue 正文摘录

### Your current environment 单机一张3090一张2080ti 22g 执行vllm serve /home/a/lmdeploy/InternVL2-8B --dtype auto --max-model-len 8192 --api-key token-abc123 --gpu_memory_utilization 1 --trust-remote-code --port 23333 --tensor-parallel-size 2 --enforce-eager --dtype=half 启动 提问无限循环回答。 当--tensor-parallel-size 1时没有问题 ![错误1](https://github.com/user-attachments/assets/3b9d1219-547a-4357-8259-7e626eb15c67) ![错误2](https://github.com/user-attachments/assets/bc1ab725-7b6b-4034-8f32-9d077974e8ee) ### 🐛 Describe the bug INFO 08-09 18:47:10 logger.py:36] Received request chat-2ace427447e347df91be974ae56f34ce: prompt: ' system\n\nCurrent model: /home/a/lmdeploy/InternVL2-8B\nCurrent date: 2024-08-09T10:47:10.457Z\n\nYou are a helpful assistant. You can help me by answering my questions. You can also ask me questions. \n user\n你好 \n assistant\n', params: SamplingParams(n=1, best_of=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.7, top_p=1.0, top_k=-1, min_p=0.0, seed=None, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=8116, min_tokens=0, logprobs=None, pro...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: internvl2-8b 提问无限循环回答 bug ### Your current environment 单机一张3090一张2080ti 22g 执行vllm serve /home/a/lmdeploy/InternVL2-8B --dtype auto --max-model-len 8192 --api-key token-abc123 --gpu_memory_utilization 1 --trust-r...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 8ee) ### 🐛 Describe the bug INFO 08-09 18:47:10 logger.py:36] Received request chat-2ace427447e347df91be974ae56f34ce: prompt: ' system\n\nCurrent model: /home/a/lmdeploy/InternVL2-8B\nCurrent date: 2024-08-09T10:47:10.4...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: _tokens=8116, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None), prompt_token_ids: [1, 92543, 9081, 402, 5564, 1762, 334, 740,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: nment 单机一张3090一张2080ti 22g 执行vllm serve /home/a/lmdeploy/InternVL2-8B --dtype auto --max-model-len 8192 --api-key token-abc123 --gpu_memory_utilization 1 --trust-remote-code --port 23333 --tensor-parallel-size 2 --enfor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: , temperature=0.7, top_p=1.0, top_k=-1, min_p=0.0, seed=None, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=8...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
