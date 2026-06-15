# vllm-project/vllm#35633: [Bug]: parity with cuda: rocm image missing amd quark kimi k2.5 mxfp4

| 字段 | 值 |
| --- | --- |
| Issue | [#35633](https://github.com/vllm-project/vllm/issues/35633) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;import_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: parity with cuda: rocm image missing amd quark kimi k2.5 mxfp4

### Issue 正文摘录

### Your current environment v0.16 kimi mi355 ### 🐛 Describe the bug hi @powderluv @chunfangamd @andyluo7 One of the main features of AMD's latest flagship MI355X GPU is MXFP4, the ability to have better perf at similar accuracy. Today i was trying to test out amd's mxfp4 checkpoint `amd/Kimi-K2.5-MXFP4` using amd's `vllm/vllm-openai-rocm:v0.16.0` but unfortunately it doesnt work out of the box due to missing amd-quark package in the docker image along with other errors. Can u take a look? seems like adding amd-quark to dockerfile.rocm would fix this ``` (Worker_TP0 pid=2820752) ERROR 03-01 01:15:53 [multiproc_executor.py:863] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/layers/fused_moe/fused_moe.py", line 1436, in outplace_fused_experts (Worker_TP0 pid=2820752) ERROR 03-01 01:15:53 [multiproc_executor.py:863] return fused_experts_impl( (Worker_TP0 pid=2820752) ERROR 03-01 01:15:53 [multiproc_executor.py:863] ^^^^^^^^^^^^^^^^^^^ (Worker_TP0 pid=2820752) ERROR 03-01 01:15:53 [multiproc_executor.py:863] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/layers/fused_moe/fused_moe.py", line 1726, in fused_experts_impl (Worker_TP0 pid=2820752) ERRO...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ly it doesnt work out of the box due to missing amd-quark package in the docker image along with other errors. Can u take a look? seems like adding amd-quark to dockerfile.rocm would fix this ``` (Worker_TP0 pid=2820752...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: parity with cuda: rocm image missing amd quark kimi k2.5 mxfp4 bug;rocm ### Your current environment v0.16 kimi mi355 ### 🐛 Describe the bug hi @powderluv @chunfangamd @andyluo7 One of the main features of AMD's...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: parity with cuda: rocm image missing amd quark kimi k2.5 mxfp4 bug;rocm ### Your current environment v0.16 kimi mi355 ### 🐛 Describe the bug hi @powderluv @chunfangamd @andyluo7 One of the main features of AMD's...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: /usr/local/lib/python3.12/dist-packages/vllm/model_executor/layers/fused_moe/fused_moe.py", line 1436, in outplace_fused_experts (Worker_TP0 pid=2820752) ERROR 03-01 01:15:53 [multiproc_executor.py:863] return fused_exp...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: i @powderluv @chunfangamd @andyluo7 One of the main features of AMD's latest flagship MI355X GPU is MXFP4, the ability to have better perf at similar accuracy. Today i was trying to test out amd's mxfp4 checkpoint `amd/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
