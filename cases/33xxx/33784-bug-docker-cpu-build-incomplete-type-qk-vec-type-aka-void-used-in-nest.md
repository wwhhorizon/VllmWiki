# vllm-project/vllm#33784: [Bug]: [Docker.cpu build] incomplete type ‘qk_vec_type’ {aka ‘void’} used in nested name specifier

| 字段 | 值 |
| --- | --- |
| Issue | [#33784](https://github.com/vllm-project/vllm/issues/33784) |
| 状态 | closed |
| 标签 | bug;cpu |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [Docker.cpu build] incomplete type ‘qk_vec_type’ {aka ‘void’} used in nested name specifier

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hello 👋 I am tryin to create custom (with my AVX flags) docker image for mainly arm64 and amd64 architecture following [this tutorial](https://docs.vllm.ai/en/stable/getting_started/installation/cpu/#build-image-from-source). Here is the problem, because I am using arm64 architecture the amd64 has to be done by emulator. When doin it, following error occurs: ```bash 464.8 Using MAX_JOBS=32 as the number of jobs. 495.4 [1/9] Building CXX object CMakeFiles/_C.dir/csrc/cpu/mla_decode.cpp.o 495.4 FAILED: [code=1] CMakeFiles/_C.dir/csrc/cpu/mla_decode.cpp.o 495.4 ccache /usr/bin/g++-12 -DPy_LIMITED_API=3 -DTORCH_EXTENSION_NAME=_C -DUSE_C10D_GLOO -DUSE_DISTRIBUTED -DUSE_RPC -DUSE_TENSORPIPE -D_C_EXPORTS -I/vllm-workspace/csrc -isystem /opt/uv/python/cpython-3.12.12-linux-x86_64-gnu/include/python3.12 -isystem /opt/venv/lib/python3.12/site-packages/torch/include -isystem /opt/venv/lib/python3.12/site-packages/torch/include/torch/csrc/api/include -O2 -g -DNDEBUG -std=gnu++17 -fPIC -mf16c -fopenmp -DVLLM_CPU_EXTENSION -mavx2 -MD -MT CMakeFiles/_C.dir/csrc/cpu/mla_decode.cpp.o -MF CMakeFiles/_C.dir/csrc/cpu/mla_decode.cpp.o.d -o CMakeFiles...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: [Docker.cpu build] incomplete type ‘qk_vec_type’ {aka ‘void’} used in nested name specifier bug;cpu ### Your current environment ### 🐛 Describe the bug Hello 👋 I am tryin to create custom (with my AVX flags) dock...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: , const int*, const int*, int, int, int, int, int) [with scalar_t = c10::BFloat16; int HEAD_DIM = 576; int V_HEAD_DIM = 512; int BLOCK_SIZE = 16]’: 495.4 /vllm-workspace/csrc/cpu/mla_decode.cpp:378:3: required from here...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: scalar_t = c10::BFloat16; int HEAD_DIM = 576; int V_HEAD_DIM = 512; int BLOCK_SIZE = 16]’: 495.4 /vllm-workspace/csrc/cpu/mla_decode.cpp:378:3: required from here 495.4 /vllm-workspace/csrc/cpu/mla_decode.cpp:259:44: er...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: reate custom (with my AVX flags) docker image for mainly arm64 and amd64 architecture following [this tutorial](https://docs.vllm.ai/en/stable/getting_started/installation/cpu/#build-image-from-source). Here is the prob...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ^~~~~~~~~~~~ 497.2 [2/9] Building CXX object CMakeFiles/_C.dir/csrc/moe/dynamic_4bit_int_moe_cpu.cpp.o 499.4 [3/9] Building CXX object CMakeFiles/_C.dir/csrc/cpu/utils.cpp.o 501.7 [4/9] Building CXX object CMakeFiles/_C...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
