# vllm-project/vllm#35599: [Bug]: cpu version compile failed in 0.16.0

| 字段 | 值 |
| --- | --- |
| Issue | [#35599](https://github.com/vllm-project/vllm/issues/35599) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;moe |
| 子分类 | env_compat |
| Operator 关键词 | activation;cuda;moe;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: cpu version compile failed in 0.16.0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug [1/9] Building CXX object CMakeFiles/_C.dir/csrc/cpu/mla_decode.cpp.o FAILED: [code=1] CMakeFiles/_C.dir/csrc/cpu/mla_decode.cpp.o /usr/bin/g++ -DPy_LIMITED_API=3 -DTORCH_EXTENSION_NAME=_C -DUSE_C10D_GLOO -DUSE_DISTRIBUTED -DUSE_RPC -DUSE_TENSORPIPE -D_C_EXPORTS -I/home/10102067/vllm-0.16.0/csrc -isystem /root/.local/share/uv/python/cpython-3.10.19-linux-x86_64-gnu/include/python3.10 -isystem /home/10102067/vllm-0.16.0/.venv/lib/python3.10/site-packages/torch/include -isystem /home/10102067/vllm-0.16.0/.venv/lib/python3.10/site-packages/torch/include/torch/csrc/api/include -mno-avx512f -mno-avx512vl -mno-avx512bw -mno-avx512dq -mno-avx512cd -O2 -g -DNDEBUG -std=gnu++17 -fPIC -mf16c -fopenmp -DVLLM_CPU_EXTENSION -mavx2 -MD -MT CMakeFiles/_C.dir/csrc/cpu/mla_decode.cpp.o -MF CMakeFiles/_C.dir/csrc/cpu/mla_decode.cpp.o.d -o CMakeFiles/_C.dir/csrc/cpu/mla_decode.cpp.o -c /home/10102067/vllm-0.16.0/csrc/cpu/mla_decode.cpp /home/10102067/vllm-0.16.0/csrc/cpu/mla_decode.cpp: In instantiation of ‘void mla_decode_kvcache_cpu_impl(scalar_t*, const scalar_t*, const scalar_t*, int, float, const int*, const int*, int, int, int, int, int) [wit...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: cpu version compile failed in 0.16.0 bug ### Your current environment ### 🐛 Describe the bug [1/9] Building CXX object CMakeFiles/_C.dir/csrc/cpu/mla_decode.cpp.o FAILED: [code=1] CMakeFiles/_C.dir/csrc/cpu/mla_de
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: t int*, const int*, int, int, int, int, int) [with scalar_t = c10::BFloat16; int HEAD_DIM = 576; int V_HEAD_DIM = 512; int BLOCK_SIZE = 16]’: /home/10102067/vllm-0.16.0/csrc/cpu/mla_decode.cpp:387:3: required from here...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: scalar_t = c10::BFloat16; int HEAD_DIM = 576; int V_HEAD_DIM = 512; int BLOCK_SIZE = 16]’: /home/10102067/vllm-0.16.0/csrc/cpu/mla_decode.cpp:387:3: required from here 391 | mla_decode_kvcache_cpu_impl ( | ~~~~~~~~~~~~~...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: uild;frontend_api;hardware_porting;model_support;moe activation;cuda;moe;triton build_error dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
