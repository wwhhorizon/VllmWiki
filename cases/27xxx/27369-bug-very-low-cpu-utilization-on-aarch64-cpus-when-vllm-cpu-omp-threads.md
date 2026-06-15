# vllm-project/vllm#27369: [Bug]: Very low CPU utilization on AArch64 CPUs when VLLM_CPU_OMP_THREADS_BIND is set

| 字段 | 值 |
| --- | --- |
| Issue | [#27369](https://github.com/vllm-project/vllm/issues/27369) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Very low CPU utilization on AArch64 CPUs when VLLM_CPU_OMP_THREADS_BIND is set

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug On AArch64 (e.g. Neoverse-V2), when `VLLM_CPU_OMP_THREADS_BIND` is set, only the first core is utilized at 100% while the other cores have very low utilization. - This behavior only happens when `VLLM_CPU_OMP_THREADS_BIND` is set - The low utilization goes away if we preload libgomp, i.e. `LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libgomp.so.1` **Example reproducer:** ``` VLLM_CPU_OMP_THREADS_BIND=0-63 VLLM_TARGET_DEVICE=cpu VLLM_CPU_KVCACHE_SPACE=32 vllm bench throughput --num-prompts 64 --seed 0 --dataset-name sharegpt --max-model-len 4096 --dataset-path ShareGPT_V3_unfiltered_cleaned_split_no_imsorry.json --model meta-llama/Llama-3.1-8B-Instruct --load-format dummy ``` **Root cause(s):** Running the reproducer above with `LD_DEBUG=libs,files` shows that there's 2 libgomp runtimes in use: - `libtorch.so` loads `libgomp-947d5fa1.so.1.0.0` (this is the libgomp that gets shipped with the PyTorch wheel) - `libarm_compute.so` (now built with vllm since #27183): loads system libgomp: `/usr/lib/aarch64-linux-gnu/libgomp.so.1` - `/tmp/torchinductor_fadara01/t3/ct3zsq772eznxbeuvpmce7lpbxrem55qxducdrdo2io7itgal3sq.main.so` (from inductor whi...

## 现有链接修复摘要

#27183 [cpu] Dispatch un-quantized linear to oneDNN/ACL by default for AArch64

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: 7d5fa1.so.1.0.0` (this is the libgomp that gets shipped with the PyTorch wheel) - `libarm_compute.so` (now built with vllm since #27183): loads system libgomp: `/usr/lib/aarch64-linux-gnu/libgomp.so.1` - `/tmp/torchindu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Very low CPU utilization on AArch64 CPUs when VLLM_CPU_OMP_THREADS_BIND is set bug ### Your current environment ### 🐛 Describe the bug On AArch64 (e.g. Neoverse-V2), when `VLLM_CPU_OMP_THREADS_BIND` is set, only...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ench throughput --num-prompts 64 --seed 0 --dataset-name sharegpt --max-model-len 4096 --dataset-path ShareGPT_V3_unfiltered_cleaned_split_no_imsorry.json --model meta-llama/Llama-3.1-8B-Instruct --load-format dummy ```...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: em55qxducdrdo2io7itgal3sq.main.so` (from inductor which is torch.compile backend for CPU) loads system libgomp: `/usr/lib/aarch64-linux-gnu/libgomp.so.1` **Suggested Fix:** All .so libraries should link against PyTorch'...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: speculative_decoding cuda;operator;sampling build_error;nan_inf;slowdown dtype;env_dependency #27183 [cpu] Dispatch un-quantized linear to oneDNN/ACL by default for AArch64 Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#27183](https://github.com/vllm-project/vllm/pull/27183) | mentioned | 0.45 | [cpu] Dispatch un-quantized linear to oneDNN/ACL by default for AArch64 | h the pytorch wheel) - `libarm_compute.so` (now built with vllm since #27183): loads system libgomp: `/usr/lib/aarch64-linux-gnu/libgomp.so.1` - `/tmp/torchinductor_fadara01/t3/ct… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
