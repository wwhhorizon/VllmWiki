# vllm-project/vllm#19123: [Bug]: Failed to start vLLM v1 with Ray. Encountered the following error: `KeyError: 'bundles'`

| 字段 | 值 |
| --- | --- |
| Issue | [#19123](https://github.com/vllm-project/vllm/issues/19123) |
| 状态 | closed |
| 标签 | bug;ray |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Failed to start vLLM v1 with Ray. Encountered the following error: `KeyError: 'bundles'`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```text import ray import os import time from ray.util.placement_group import placement_group from ray.util.scheduling_strategies import PlacementGroupSchedulingStrategy from vllm import LLM, SamplingParams os.environ["VLLM_USE_V1"] = "1" os.environ["CUDA_VISIBLE_DEVICES"] = "1" ray.init() pg = placement_group([{"CPU": 0, "GPU": 1}]) ray.get(pg.ready()) strategy = PlacementGroupSchedulingStrategy( placement_group=pg, placement_group_capture_child_tasks=True, placement_group_bundle_index=0, ) llm = ray.remote( num_cpus=0, num_gpus=0, scheduling_strategy=strategy, )(LLM).remote( model="/root/.cache/modelscope/hub/models/facebook/opt-125m", tokenizer="/root/.cache/modelscope/hub/models/facebook/opt-125m", enforce_eager=True, tensor_parallel_size=1, distributed_executor_backend="ray", dtype="float16", ) prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0) time.sleep(5) outputs = ray.get(llm.generate.remote(prompts, sampling_params)) print("-" * 50) for output in outputs: prompt = output.prompt generated_text = out...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: bug;ray ### Your current environment ### 🐛 Describe the bug ```text import ray import os import time from ray.util.placement_group import placement_group from ray.util.scheduling_strategies import PlacementGroupScheduli...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: , num_gpus=0, scheduling_strategy=strategy, )(LLM).remote( model="/root/.cache/modelscope/hub/models/facebook/opt-125m", tokenizer="/root/.cache/modelscope/hub/models/facebook/opt-125m", enforce_eager=True, tensor_paral...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: tensor_parallel_size=1, distributed_executor_backend="ray", dtype="float16", ) prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_para...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: 'generate'. (LLM pid=95366) INFO 06-04 02:46:30 [config.py:1697] Chunked prefill is enabled with max_num_batched_tokens=8192. (LLM pid=95366) WARNING 06-04 02:46:30 [cuda.py:95] To see benefits of async output processin...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: force_eager=True, tensor_parallel_size=1, distributed_executor_backend="ray", dtype="float16", ) prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
