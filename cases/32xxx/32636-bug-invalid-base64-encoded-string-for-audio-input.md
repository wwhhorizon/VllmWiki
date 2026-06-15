# vllm-project/vllm#32636: [Bug]: Invalid base64-encoded string for audio input

| 字段 | 值 |
| --- | --- |
| Issue | [#32636](https://github.com/vllm-project/vllm/issues/32636) |
| 状态 | open |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Invalid base64-encoded string for audio input

### Issue 正文摘录

### Your current environment vllm 0.13.0 ### 🐛 Describe the bug I install vllm 0.13.0 version by pip. And I use the following commands to deploy Qwen3-Omni-30B-A3B-Instruct model: ``` VLLM_USE_MODELSCOPE=true vllm serve /xxx/Qwen3-Omni-30B-A3B-Instruct \ --port "8000" \ --dtype bfloat16 \ --max-model-len 32768 \ --tensor-parallel-size 1 \ --gpu-memory-utilization 0.8 \ --served-model-name Qwen3-Omni-30B-A3B-Instruct\ --trust-remote-code ``` Then I use evalscope to eval omni_bench (using use_audio as input): ``` from evalscope import TaskConfig, run_task from evalscope.constants import EvalType task_cfg = TaskConfig( model='Qwen3-Omni-30B-A3B-Instruct', api_url='http://localhost:8000/v1', api_key='EMPTY', eval_type=EvalType.SERVICE, datasets=[ 'omni_bench', ], dataset_args={ 'omni_bench': { 'extra_params': { 'use_image': False, # Whether to use image input, if False, use text alternative image content. 'use_audio': True, # Whether to use audio input, if False, use text alternative audio content. } } }, eval_batch_size=1, generation_config={ 'max_tokens': 10000, # Maximum number of tokens to generate, recommended to set a large value to avoid output truncation 'temperature': 0.0, #...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: bug ### Your current environment vllm 0.13.0 ### 🐛 Describe the bug I install vllm 0.13.0 version by pip. And I use the following commands to deploy Qwen3-Omni-30B-A3B-Instruct model: ``` VLLM_USE_MODELSCOPE=true vllm s...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: vllm serve /xxx/Qwen3-Omni-30B-A3B-Instruct \ --port "8000" \ --dtype bfloat16 \ --max-model-len 32768 \ --tensor-parallel-size 1 \ --gpu-memory-utilization 0.8 \ --served-model-name Qwen3-Omni-30B-A3B-Instruct\ --trust...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: l vllm 0.13.0 version by pip. And I use the following commands to deploy Qwen3-Omni-30B-A3B-Instruct model: ``` VLLM_USE_MODELSCOPE=true vllm serve /xxx/Qwen3-Omni-30B-A3B-Instruct \ --port "8000" \ --dtype bfloat16 \ -...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ame Qwen3-Omni-30B-A3B-Instruct\ --trust-remote-code ``` Then I use evalscope to eval omni_bench (using use_audio as input): ``` from evalscope import TaskConfig, run_task from evalscope.constants import EvalType task_c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ly. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
