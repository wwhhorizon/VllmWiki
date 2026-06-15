# vllm-project/vllm#13722: [Bug]: Speculative Decoding: device="cuda:1" will encounter "RuntimeError: CUDA error: an illegal memory access was encountered"

| 字段 | 值 |
| --- | --- |
| Issue | [#13722](https://github.com/vllm-project/vllm/issues/13722) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Speculative Decoding: device="cuda:1" will encounter "RuntimeError: CUDA error: an illegal memory access was encountered"

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I set `device='cuda:1'`, the speculative decoding will result in "RuntimeError: CUDA error: an illegal memory access was encountered", but `device='cuda:0'` is fine. ```python llm = LLM( model="Qwen/Qwen2.5-3B-Instruct", speculative_model="Qwen/Qwen2.5-0.5B-Instruct", num_speculative_tokens=5, gpu_memory_utilization=0.7, enable_prefix_caching=True, device="cuda:1" # when set to "cuda:1" -> llm.generate will encounter "RuntimeError: CUDA error: an illegal memory access was encountered" ) ``` ``` Processed prompts: 0%| | 0/112 [00:00 [rank0]: outputs = llm.generate(prompts, sampling_params) [rank0]: File "/root/miniconda3/envs/rlhf/lib/python3.10/site-packages/vllm/utils.py", line 1074, in inner [rank0]: return fn(*args, **kwargs) [rank0]: File "/root/miniconda3/envs/rlhf/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 467, in generate [rank0]: outputs = self._run_engine(use_tqdm=use_tqdm) [rank0]: File "/root/miniconda3/envs/rlhf/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 1388, in _run_engine [rank0]: step_outputs = self.llm_engine.step() [rank0]: File "/root/miniconda3/envs/rlhf/lib/python3.10/si...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [rank0]: For debugging consider passing CUDA_LAUNCH_BLOCKING=1 [rank0]: Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ``` ### Before submitting a new issue... - [x] Make sure you already searched f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Speculative Decoding: device="cuda:1" will encounter "RuntimeError: CUDA error: an illegal memory access was encountered" bug ### Your current environment ### 🐛 Describe the bug When I set `device='cuda:1'`, the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ncountered", but `device='cuda:0'` is fine. ```python llm = LLM( model="Qwen/Qwen2.5-3B-Instruct", speculative_model="Qwen/Qwen2.5-0.5B-Instruct", num_speculative_tokens=5, gpu_memory_utilization=0.7, enable_prefix_cach...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Speculative Decoding: device="cuda:1" will encounter "RuntimeError: CUDA error: an illegal memory access was encountered" bug ### Your current environment ### 🐛 Describe the bug When I set `device='cuda:1'`, the...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tend_api;hardware_porting;model_support;speculative_decoding cuda;kernel;triton build_error;crash;mismatch env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
