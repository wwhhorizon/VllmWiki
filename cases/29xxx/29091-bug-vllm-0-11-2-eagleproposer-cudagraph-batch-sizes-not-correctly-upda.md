# vllm-project/vllm#29091: [Bug]: vLLM 0.11.2 EagleProposer.cudagraph_batch_sizes not correctly updated

| 字段 | 值 |
| --- | --- |
| Issue | [#29091](https://github.com/vllm-project/vllm/issues/29091) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;moe |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM 0.11.2 EagleProposer.cudagraph_batch_sizes not correctly updated

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Bug Description In `vllm\v1\spec_decode\eagle.py`, the `EagleProposer` depends on `CompilationConfig.cudagraph_capture_sizes`: ``` class EagleProposer: def __init__( self, vllm_config: VllmConfig, device: torch.device, runner=None, ): ... self.cudagraph_batch_sizes = ( (sorted(self.vllm_config.compilation_config.cudagraph_capture_sizes)) if self.use_cuda_graph else [] ) ``` When speculative decoding is enabled, the `GPUModelRunner` calls the `CompilationConfig.adjust_cudagraph_sizes_for_spec_decode` function, which modifies `max_cudagraph_capture_size` and `cudagraph_capture_sizes`. ``` # vllm\config\compilation.py` class CompilationConfig: .... def adjust_cudagraph_sizes_for_spec_decode( self, uniform_decode_query_len: int, tensor_parallel_size: int ): ...... self.max_cudagraph_capture_size = rounded_sizes[-1] self.cudagraph_capture_sizes = rounded_sizes # Recompute after adjusting the cudagraph sizes self.compute_bs_to_padded_graph_size() ``` However, `GPUModelRunner.drafter.cudagraph_batch_sizes` (`EagleProposer`) is not correctly updated. This causes the subsequent logic to evaluate as True, incorrectly calling `self.vllm_...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: vLLM 0.11.2 EagleProposer.cudagraph_batch_sizes not correctly updated bug ### Your current environment ### 🐛 Describe the bug ## Bug Description In `vllm\v1\spec_decode\eagle.py`, the `EagleProposer` depends on `...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ronment ### 🐛 Describe the bug ## Bug Description In `vllm\v1\spec_decode\eagle.py`, the `EagleProposer` depends on `CompilationConfig.cudagraph_capture_sizes`: ``` class EagleProposer: def __init__( self, vllm_config:...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Offer personalized meal planning and ingredient delivery services for specific dietary needs and conditions, such as celiac disease\nEstablish a research and development team to continuously improve product offerings an...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: llm\v1\spec_decode\eagle.py`, the `EagleProposer` depends on `CompilationConfig.cudagraph_capture_sizes`: ``` class EagleProposer: def __init__( self, vllm_config: VllmConfig, device: torch.device, runner=None, ): ... s...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: l planning services through partnerships with leading food and nutrition experts\nEstablish partnerships with health insurance providers and fitness centers to offer incentives to users\n\n4. \\*\\*Year 4:\\*\\* Explore...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
