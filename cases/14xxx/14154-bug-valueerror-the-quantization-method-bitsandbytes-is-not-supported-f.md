# vllm-project/vllm#14154: [Bug]: ValueError: The quantization method bitsandbytes is not supported for the current GPU. Minimum capability: 70. Current capability: 52.

| 字段 | 值 |
| --- | --- |
| Issue | [#14154](https://github.com/vllm-project/vllm/issues/14154) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError: The quantization method bitsandbytes is not supported for the current GPU. Minimum capability: 70. Current capability: 52.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug VLLM doesn't seem to support bitsandbytes for 4060Ti. Specifically trying to run `unsloth/gemma-2-2b-bnb-4bit` config.json: 100%|█████████████████████████████████████████████| 1.37k/1.37k [00:00 llm = LLM( ^^^^ File "/home/jay/anaconda3/envs/vllm_3.12/lib/python3.12/site-packages/vllm/utils.py", line 1022, in inner return fn(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^ File "/home/jay/anaconda3/envs/vllm_3.12/lib/python3.12/site-packages/vllm/entrypoints/llm.py", line 242, in __init__ self.llm_engine = self.engine_class.from_engine_args( ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/jay/anaconda3/envs/vllm_3.12/lib/python3.12/site-packages/vllm/engine/llm_engine.py", line 486, in from_engine_args engine_config = engine_args.create_engine_config(usage_context) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/jay/anaconda3/envs/vllm_3.12/lib/python3.12/site-packages/vllm/engine/arg_utils.py", line 1334, in create_engine_config config = VllmConfig( ^^^^^^^^^^^ File " ", line 19, in __init__ File "/home/jay/anaconda3/envs/vllm_3.12/lib/python3.12/site-packages/vllm/config.py", line 3279, in __post_init__ self.quant_config = Vllm...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: scribe the bug VLLM doesn't seem to support bitsandbytes for 4060Ti. Specifically trying to run `unsloth/gemma-2-2b-bnb-4bit` config.json: 100%|█████████████████████████████████████████████| 1.37k/1.37k [00:00 llm = LLM...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: zation method bitsandbytes is not supported for the current GPU. Minimum capability: 70. Current capability: 52. bug;stale ### Your current environment ### 🐛 Describe the bug VLLM doesn't seem to support bitsandbytes fo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: to support bitsandbytes for 4060Ti. Specifically trying to run `unsloth/gemma-2-2b-bnb-4bit` config.json: 100%|█████████████████████████████████████████████| 1.37k/1.37k [00:00 llm = LLM( ^^^^ File "/home/jay/anaconda3/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: for the current GPU. Minimum capability: 70. Current capability: 52. bug;stale ### Your current environment ### 🐛 Describe the bug VLLM doesn't seem to support bitsandbytes for 4060Ti. Specifically trying to run `unslot...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;crash;nan_inf;slowdown env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
