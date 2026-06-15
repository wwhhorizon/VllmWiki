# vllm-project/vllm#35746: [Bug]: Segfault at IP=0 during model warmup on AVX512_BF16 host (AMD 7940HS)

| 字段 | 值 |
| --- | --- |
| Issue | [#35746](https://github.com/vllm-project/vllm/issues/35746) |
| 状态 | closed |
| 标签 | bug;cpu |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Segfault at IP=0 during model warmup on AVX512_BF16 host (AMD 7940HS)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I came across this problem trying out the Qwen3:0.6B model on my machine. I started the server by command: `VLLM_CPU_KVCACHE_SPACE=1 vllm serve Qwen/Qwen3-0.6B --dtype=bfloat16 --max-model-len=128` and got error like the `dmesg -T` yields logs like: ``` [一 3月 2 20:25:46 2026] VLLM::EngineCor[1024641]: segfault at 0 ip 0000000000000000 sp 00007ffec640f458 error 14 likely on CPU 8 (core 0, socket 0) [一 3月 2 20:25:46 2026] Code: Unable to access opcode bytes at 0xffffffffffffffd6. ``` I noticed that there're some missing `so`s: ``` (base) [netwilliam@NWm-AE7 vllm]$ ldd ./_C.abi3.so linux-vdso.so.1 (0x000071e155eb0000) libnuma.so.1 => /lib/x86_64-linux-gnu/libnuma.so.1 (0x000071e155e74000) libc10.so => not found libtorch_cpu.so => not found libtorch.so => not found libstdc++.so.6 => /lib/x86_64-linux-gnu/libstdc++.so.6 (0x000071e154200000) libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x000071e154517000) libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x000071e155e44000) libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x000071e153e00000) /lib64/ld-linux-x86-64.so.2 (0x000071e155eb2000) ``` by setting up the `LD_LIBRARY_PATH` I go...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ens inside a generated kernel by Torch Inductor. It appears that the JIT-compiled code is attempting to call a null function pointer, possibly related to AVX512_BF16 vectorization or oneDNN integration on this AMD Zen4...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Segfault at IP=0 during model warmup on AVX512_BF16 host (AMD 7940HS) bug;cpu ### Your current environment ### 🐛 Describe the bug I came across this problem trying out the Qwen3:0.6B model on my machine. I starte...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 6 (0x000071e153e00000) /lib64/ld-linux-x86-64.so.2 (0x000071e155eb2000) ``` by setting up the `LD_LIBRARY_PATH` I got it squared ``` (base) [netwilliam@NWm-AE7 vllm]$ ldd ./_C.abi3.so linux-vdso.so.1 (0x000079db83457000...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Segfault at IP=0 during model warmup on AVX512_BF16 host (AMD 7940HS) bug;cpu ### Your current environment ### 🐛 Describe the bug I came across this problem trying out the Qwen3:0.6B model on my machine. I starte...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cache;cuda;kernel;operator;sampling;triton build_error;crash;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
