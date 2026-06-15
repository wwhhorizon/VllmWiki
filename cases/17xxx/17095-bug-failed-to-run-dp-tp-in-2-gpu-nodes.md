# vllm-project/vllm#17095: [Bug]: Failed to run dp+tp in 2 GPU Nodes

| 字段 | 值 |
| --- | --- |
| Issue | [#17095](https://github.com/vllm-project/vllm/issues/17095) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe;quantization;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Failed to run dp+tp in 2 GPU Nodes

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I tried to run deepseek-r1 mode with vllm+ray cluster in 2 GPU nodes. Each node has 8 GPUs. The goal is to run ds-v1 with tensor parallel + data parallel in 2 nodes. The command used： ``` vllm serve /home/deepseek-ai/ --port 8080 **--tensor-parallel-size 8 -dp 2** --gpu_memory_utilization=0.98 --trust-remote-code --host 0.0.0.0 ``` Note: CUDA_VISIBLE_DEVICES is not set in each node environment. Error log as below: ======device_id_to_phy_device_id===========device_id====== 0 =======device_id_to_phy_device_id==========CUDA_VISIBLE_DEVICES in env: 8,9,10,11,12,13,14,15 =======device_id_to_phy_devcie_id======device_ids: ['8', '9', '10', '11', '12', '13', '14', '15'] ======device_id_to_phy_device_id===========phy_devcie_id====== 8 ===============get_device_cap()=======send device_id: 0 ===============get_device_cap()=======get phy_device_id: 8 -----------get_device_cap -----> device_id_to_phy_device_id: ======device_id_to_phy_device_id===========device_id====== 0 =======device_id_to_phy_device_id==========CUDA_VISIBLE_DEVICES in env: 0,1,2,3,4,5,6,7 =======device_id_to_phy_devcie_id======device_ids: ['0', '1', '2', '3', '4', '5', '6',...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: VISIBLE_DEVICES in env: 8,9,10,11,12,13,14,15 =======device_id_to_phy_devcie_id======device_ids: ['8', '9', '10', '11', '12', '13', '14', '15'] ======device_id_to_phy_device_id===========phy_devcie_id====== 8 ==========...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: emory_utilization=0.98 --trust-remote-code --host 0.0.0.0 ``` Note: CUDA_VISIBLE_DEVICES is not set in each node environment. Error log as below: ======device_id_to_phy_device_id===========device_id====== 0 =======devic...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/layers/quantization/fp8.py", line 15, in from vllm.model_executor.layers.fused_moe import (FusedMoE, FusedMoEMethodBase, File "/usr/local/lib/python3.12/...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: ization/fp8.py", line 15, in from vllm.model_executor.layers.fused_moe import (FusedMoE, FusedMoEMethodBase, File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/layers/fused_moe/__init__.py", line 6, in fr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Failed to run dp+tp in 2 GPU Nodes bug;stale ### Your current environment ### 🐛 Describe the bug I tried to run deepseek-r1 mode with vllm+ray cluster in 2 GPU nodes. Each node has 8 GPUs. The goal is to run ds-v...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
