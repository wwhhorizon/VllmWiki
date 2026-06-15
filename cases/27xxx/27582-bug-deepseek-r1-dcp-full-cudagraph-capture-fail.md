# vllm-project/vllm#27582: [Bug]: Deepseek-R1 DCP full cudagraph capture fail

| 字段 | 值 |
| --- | --- |
| Issue | [#27582](https://github.com/vllm-project/vllm/issues/27582) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Deepseek-R1 DCP full cudagraph capture fail

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Full CUDA graph capture causes vLLM to fail to launch with DCP. I used the same DCP size as suggested in the official instructions. The crash appears to happen when we are in the section of CUDA full graph capture. Short section of the log pasted here(Full log attached as well) : [deepseek-r1-debug-vllm-0.11.0-release.log](https://github.com/user-attachments/files/23167124/deepseek-r1-debug-vllm-0.11.0-release.log) ): ``` [1;36m(Worker_TP0 pid=1356725)[0;0m ERROR 10-27 14:10:45 [multiproc_executor.py:671] File "/root/thibrahi/debug_deepseek_dcp/lib64/python3.12/site-packages/vllm/v1/attention/backends/mla/common.py", line 1779, in forward [1;36m(Worker_TP0 pid=1356725)[0;0m ERROR 10-27 14:10:45 [multiproc_executor.py:671] attn_out = cp_lse_ag_out_rs(attn_out, lse, get_dcp_group()) [1;36m(Worker_TP0 pid=1356725)[0;0m ERROR 10-27 14:10:45 [multiproc_executor.py:671] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [1;36m(Worker_TP0 pid=1356725)[0;0m ERROR 10-27 14:10:45 [multiproc_executor.py:671] File "/root/thibrahi/debug_deepseek_dcp/lib64/python3.12/site-packages/vllm/attention/ops/common.py", line 138, in cp_lse_ag_out...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ail to launch with DCP. I used the same DCP size as suggested in the official instructions. The crash appears to happen when we are in the section of CUDA full graph capture. Short section of the log pasted here(Full lo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rahi/debug_deepseek_dcp/lib64/python3.12/site-packages/vllm/v1/attention/backends/mla/common.py", line 1779, in forward [1;36m(Worker_TP0 pid=1356725)[0;0m ERROR 10-27 14:10:45 [multiproc_executor.py:671] attn_out = c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Deepseek-R1 DCP full cudagraph capture fail bug ### Your current environment ### 🐛 Describe the bug Full CUDA graph capture causes vLLM to fail to launch with DCP. I used the same DCP size as suggested in the off...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [0;0m ERROR 10-27 14:10:45 [multiproc_executor.py:671] attn_out = cp_lse_ag_out_rs(attn_out, lse, get_dcp_group()) [1;36m(Worker_TP0 pid=1356725)[0;0m ERROR 10-27 14:10:45 [multiproc_executor.py:671] ^^^^^^^^^^^^^^^^^...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ctness attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding attention;cuda;kernel;operator;sampling;triton build_error;crash;nan_inf env_dependency Your cu...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
