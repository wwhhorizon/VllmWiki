# vllm-project/vllm#32311: [Bug/Question]: Unexpected CUDA Graph Replay observed only in the first request's prefill under PIECEWISE mode

| 字段 | 值 |
| --- | --- |
| Issue | [#32311](https://github.com/vllm-project/vllm/issues/32311) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug/Question]: Unexpected CUDA Graph Replay observed only in the first request's prefill under PIECEWISE mode

### Issue 正文摘录

**Description**: I am observing inconsistent CUDA Graph behavior during the prefill stage when using `PIECEWISE` CUDA Graph mode. Specifically, the profiler shows `Graph Replay` during the prefill of the first request, but subsequent requests with the same input length (2000 tokens) do not trigger any graph replay in their prefill phase. Graph dispatcher logs show `cudagraph_mode=None` of prefill phase. ```bash VLLM_TORCH_PROFILER_DIR=./nv_piecewise CUDA_VISIBLE_DEVICES=5 vllm serve meta-llama/Llama-3.1-8B-Instruct --max-model-len 8192 -cc.mode=3 -cc.cudagraph_mode='PIECEWISE' vllm bench serve --backend vllm --model meta-llama/Llama-3.1-8B-Instruct --dataset-name random --random-input-len 2000 --random-output-len 10 --profile --num-prompts 10 --port 8000 --max-concurrency 1 ``` ```bash ^[[0;36m(EngineCore_DP0 pid=10057)^[[0;0m DEBUG 01-14 08:25:46 [v1/worker/gpu_model_runner.py:3013] Running batch with cudagraph_mode: NONE, batch_descriptor: BatchDescriptor(num_tokens=2000, num_reqs=None, uniform=False, has_lora=False), should_ubatch: False, num_tokens_across_dp: None ^[[0;36m(EngineCore_DP0 pid=10057)^[[0;0m DEBUG 01-14 08:25:46 [v1/worker/gpu_model_runner.py:3013] Running batch...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: tokens) do not trigger any graph replay in their prefill phase. Graph dispatcher logs show `cudagraph_mode=None` of prefill phase. ```bash VLLM_TORCH_PROFILER_DIR=./nv_piecewise CUDA_VISIBLE_DEVICES=5 vllm serve meta-ll...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: TORCH_PROFILER_DIR=./nv_piecewise CUDA_VISIBLE_DEVICES=5 vllm serve meta-llama/Llama-3.1-8B-Instruct --max-model-len 8192 -cc.mode=3 -cc.cudagraph_mode='PIECEWISE' vllm bench serve --backend vllm --model meta-llama/Llam...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug/Question]: Unexpected CUDA Graph Replay observed only in the first request's prefill under PIECEWISE mode usage **Description**: I am observing inconsistent CUDA Graph behavior during the prefill stage when using `...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: or during the prefill stage when using `PIECEWISE` CUDA Graph mode. Specifically, the profiler shows `Graph Replay` during the prefill of the first request, but subsequent requests with the same input length (2000 token...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Bug/Question]: Unexpected CUDA Graph Replay observed only in the first request's prefill under PIECEWISE mode usage **Description**: I am observing inconsistent CUDA Graph behavior during the prefill stage when using `...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
