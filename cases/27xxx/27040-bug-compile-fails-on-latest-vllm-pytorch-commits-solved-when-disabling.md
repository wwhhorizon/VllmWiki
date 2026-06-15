# vllm-project/vllm#27040: [Bug]: Compile fails on latest vllm/pytorch commits, solved when disabling aot_compile

| 字段 | 值 |
| --- | --- |
| Issue | [#27040](https://github.com/vllm-project/vllm/issues/27040) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Compile fails on latest vllm/pytorch commits, solved when disabling aot_compile

### Issue 正文摘录

### Your current environment ``` lsakka@devgpu009.cco5 ~/vllm (hu)]$ wget https://raw.githubusercontent.com/vllm-project/vllm/main/vllm/collect_env.py --2025-10-16 09:31:06-- https://raw.githubusercontent.com/vllm-project/vllm/main/vllm/collect_env.py Resolving fwdproxy (fwdproxy)... 2401:db00:2ff:e002:face:b00c:0:1e10 Connecting to fwdproxy (fwdproxy)|2401:db00:2ff:e002:face:b00c:0:1e10|:8080... connected. Proxy request sent, awaiting response... 200 OK Length: 28050 (27K) [text/plain] Saving to: ‘collect_env.py’ collect_env.py 100%[====================================================================>] 27.39K --.-KB/s in 0.004s 2025-10-16 09:31:06 (6.20 MB/s) - ‘collect_env.py’ saved [28050/28050] [lsakka@devgpu009.cco5 ~/vllm (hu)]$ python collect_env.py Collecting environment information... ============================== System Info ============================== OS : CentOS Stream 9 (x86_64) GCC version : (GCC) 11.5.0 20240719 (Red Hat 11.5.0-11) Clang version : 20.1.8 (CentOS 20.1.8-1.el9) CMake version : version 4.1.0 Libc version : glibc-2.34 ============================== PyTorch Info ============================== PyTorch version : 2.10.0a0+git219fb6a Is debug build : Fal...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: Compile fails on latest vllm/pytorch commits, solved when disabling aot_compile bug;torch.compile ### Your current environment ``` lsakka@devgpu009.cco5 ~/vllm (hu)]$ wget https://raw.githubusercontent.com/vllm-p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: : 2.10.0a0+git219fb6a Is debug build : False CUDA used to build PyTorch : 12.9 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.18 |...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: 24.24.12 [pip3] flake8-pyi==25.5.0 [pip3] flake8_simplify==0.22.0 [pip3] flashinfer-python==0.4.0 [pip3] mypy_extensions==1.1.0 [pip3] numpy==2.2.6 [pip3] nvidia-cudnn-frontend==1.15.0 [pip3] nvidia-cutlass-dsl==4.2.1 [...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local avx512_bf16 clzero irperf xsaveerptr rdpru wbnoinvd amd_ppin cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefil...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: gpu009.cco5 ~/vllm (hu)]$ python collect_env.py Collecting environment information... ============================== System Info ============================== OS : CentOS Stream 9 (x86_64) GCC version : (GCC) 11.5.0 20...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
