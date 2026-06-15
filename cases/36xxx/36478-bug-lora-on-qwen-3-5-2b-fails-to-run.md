# vllm-project/vllm#36478: [Bug]:  LoRA on Qwen-3.5-2B fails to run

| 字段 | 值 |
| --- | --- |
| Issue | [#36478](https://github.com/vllm-project/vllm/issues/36478) |
| 状态 | open |
| 标签 | bug |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;kernel;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  LoRA on Qwen-3.5-2B fails to run

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug shell script: ```sh export CUDA_VISIBLE_DEVICES="4" vllm serve /opt/nas/n/model/Qwen3.5-2B \ --gpu-memory-utilization 0.6 \ --host 0.0.0.0 \ --port 6688 \ --tensor-parallel-size 1 \ --max_model_len 10240 \ --allowed_local_media_path /opt/nas/n \ --enable-log-requests \ --enable-lora \ --lora-modules M1=/opt/nas/n/ms-swift/output/lora/2B/checkpoint-1640 ``` Logs: ```text (EngineCore_DP0 pid=2550193) ERROR 03-09 16:48:25 [core.py:1100] self.lora_manager.set_active_adapters(lora_requests, lora_mapping) (EngineCore_DP0 pid=2550193) ERROR 03-09 16:48:25 [core.py:1100] File "/opt/nas/p/conda/envs/xzx_vllm_qwen3_5/lib/python3.12/site-packages/vllm/lora/worker_manager.py", line 166, in set_active_adapters (EngineCore_DP0 pid=2550193) ERROR 03-09 16:48:25 [core.py:1100] self._apply_adapters(requests) (EngineCore_DP0 pid=2550193) ERROR 03-09 16:48:25 [core.py:1100] File "/opt/nas/p/conda/envs/xzx_vllm_qwen3_5/lib/python3.12/site-packages/vllm/lora/worker_manager.py", line 253, in _apply_adapters (EngineCore_DP0 pid=2550193) ERROR 03-09 16:48:25 [core.py:1100] self.add_adapter(lora) (EngineCore_DP0 pid=2550193) ERROR 03-09 16:48:25 [core.py...

## 现有链接修复摘要

#36652 Fix Qwen3.5 LoRA packed module mapping | #36825 [Bugfix] Fix Qwen3.5 LoRA IndexError in packed_modules_mapping | #37019 fix: generalize LoRA layer handling for N-way fused projections

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;gemm_linear;model_support cuda;kernel;triton build_error env_dependency;shape #36652 Fix Qwen3.5 LoRA p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rrent environment ### 🐛 Describe the bug shell script: ```sh export CUDA_VISIBLE_DEVICES="4" vllm serve /opt/nas/n/model/Qwen3.5-2B \ --gpu-memory-utilization 0.6 \ --host 0.0.0.0 \ --port 6688 \ --tensor-parallel-size...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: LoRA on Qwen-3.5-2B fails to run bug ### Your current environment ### 🐛 Describe the bug shell script: ```sh export CUDA_VISIBLE_DEVICES="4" vllm serve /opt/nas/n/model/Qwen3.5-2B \ --gpu-memory-utilization 0.6 \...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ;distributed_parallel;frontend_api;gemm_linear;model_support cuda;kernel;triton build_error env_dependency;shape #36652 Fix Qwen3.5 LoRA packed module mapping | #36825 [Bugfix] Fix Qwen3.5 LoRA IndexError in packed_modu...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: e.py:1100] self.lora_manager.set_active_adapters(lora_requests, lora_mapping) (EngineCore_DP0 pid=2550193) ERROR 03-09 16:48:25 [core.py:1100] File "/opt/nas/p/conda/envs/xzx_vllm_qwen3_5/lib/python3.12/site-packages/vl...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36652](https://github.com/vllm-project/vllm/pull/36652) | closes_keyword | 0.95 | Fix Qwen3.5 LoRA packed module mapping | fix for the crash reported in: - #36478 - #36372 ## Test Plan 1. Reproduce the issue with a Qwen3.5 model + LoRA adapter. Before this change, engine initialization fails durin |
| [#36825](https://github.com/vllm-project/vllm/pull/36825) | mentioned | 0.6 | [Bugfix] Fix Qwen3.5 LoRA IndexError in packed_modules_mapping | allelLinearWithLoRA`, but that's a larger refactor. Related: #36372, #36478 ## Test plan - [x] Verified LoRA training (TP=1) completes successfully with Qwen3.5-9B on 2x RTX PRO 6… |
| [#37019](https://github.com/vllm-project/vllm/pull/37019) | closes_keyword | 0.95 | fix: generalize LoRA layer handling for N-way fused projections | fix for free. Related: #36372, #36478, #36976 ## Test plan Tested on 2x RTX PRO 6000 Blackwell with LoRA adapters targeting GDN layers (`in_proj_qkv`, `in_proj_z`): **Qwen/Qwen |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
