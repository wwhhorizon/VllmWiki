# vllm-project/vllm#17275: [Bug]: Fail to compile the main branch and tag v0.8.4.

| 字段 | 值 |
| --- | --- |
| Issue | [#17275](https://github.com/vllm-project/vllm/issues/17275) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Fail to compile the main branch and tag v0.8.4.

### Issue 正文摘录

### Your current environment I follow the guide to build vllm with CPU inference, and get the errors during compilation. https://docs.vllm.ai/en/latest/getting_started/installation/cpu.html?device=x86 ``` -- DNNL_TARGET_ARCH: X64 -- DNNL_LIBRARY_NAME: dnnl -- Enabled testing coverage: CI -- Enabled workload: INFERENCE -- Enabled primitives: MATMUL;REORDER -- Enabled primitive CPU ISA: ALL -- Enabled primitive GPU ISA: ALL -- Enabled GeMM kernels ISA: ALL -- Primitive cache is enabled -- CPU extension compile flags: -mf16c;-fopenmp;-DVLLM_CPU_EXTENSION;-mavx512f;-mavx512vl;-mavx512bw;-mavx512dq -- Enabling C extension. -- Configuring done (3.5s) -- Generating done (0.2s) -- Build files have been written to: /root/vllm_source/build/temp.linux-x86_64-cpython-312 [1/10] Building CXX object CMakeFiles/_C.dir/csrc/cpu/activation.cpp.o FAILED: CMakeFiles/_C.dir/csrc/cpu/activation.cpp.o ccache /usr/bin/c++ -DPy_LIMITED_API=3 -DTORCH_EXTENSION_NAME=_C -DUSE_C10D_GLOO -DUSE_DISTRIBUTED -DUSE_RPC -DUSE_TENSORPIPE -D_C_EXPORTS -I/root/vllm_source/csrc -I/root/vllm_source/.deps/onednn-build/include -I/root/vllm_source/. deps/onednn-src/src/../include -isystem /root/miniconda3/envs/vllm/includ...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: Fail to compile the main branch and tag v0.8.4. bug ### Your current environment I follow the guide to build vllm with CPU inference, and get the errors during compilation. https://docs.vllm.ai/en/latest/getting_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: est/getting_started/installation/cpu.html?device=x86 ``` -- DNNL_TARGET_ARCH: X64 -- DNNL_LIBRARY_NAME: dnnl -- Enabled testing coverage: CI -- Enabled workload: INFERENCE -- Enabled primitives: MATMUL;REORDER -- Enable...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: N;-mavx512f;-mavx512vl;-mavx512bw;-mavx512dq -- Enabling C extension. -- Configuring done (3.5s) -- Generating done (0.2s) -- Build files have been written to: /root/vllm_source/build/temp.linux-x86_64-cpython-312 [1/10...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: bled primitive CPU ISA: ALL -- Enabled primitive GPU ISA: ALL -- Enabled GeMM kernels ISA: ALL -- Primitive cache is enabled -- CPU extension compile flags: -mf16c;-fopenmp;-DVLLM_CPU_EXTENSION;-mavx512f;-mavx512vl;-mav...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: rence, and get the errors during compilation. https://docs.vllm.ai/en/latest/getting_started/installation/cpu.html?device=x86 ``` -- DNNL_TARGET_ARCH: X64 -- DNNL_LIBRARY_NAME: dnnl -- Enabled testing coverage: CI -- En...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
