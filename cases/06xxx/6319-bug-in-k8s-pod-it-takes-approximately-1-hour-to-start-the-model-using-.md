# vllm-project/vllm#6319: [Bug]: In k8s pod, it takes approximately 1 hour to start the model using vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#6319](https://github.com/vllm-project/vllm/issues/6319) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;quantization;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: In k8s pod, it takes approximately 1 hour to start the model using vllm

### Issue 正文摘录

### Your current environment ### python 3.10.14 ### GPU is V100 * 4 ### nvidia-smi ``` Thu Jul 11 10:53:42 2024 +-----------------------------------------------------------------------------+ | NVIDIA-SMI 525.60.13 Driver Version: 525.60.13 CUDA Version: 12.0 | |-------------------------------+----------------------+----------------------+ | GPU Name Persistence-M| Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap| Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |===============================+======================+======================| | 0 Tesla V100-SXM2... Off | 00000000:A1:00.0 Off | 0 | | N/A 39C P0 55W / 300W | 17077MiB / 32768MiB | 0% Default | | | | N/A | +-------------------------------+----------------------+----------------------+ | 1 Tesla V100-SXM2... Off | 00000000:A2:00.0 Off | 0 | | N/A 37C P0 56W / 300W | 17029MiB / 32768MiB | 0% Default | | | | N/A | +-------------------------------+----------------------+----------------------+ | 2 Tesla V100-SXM2... Off | 00000000:A3:00.0 Off | 0 | | N/A 37C P0 54W / 300W | 17069MiB / 32768MiB | 0% Default | | | | N/A | +-------------------------------+----------------------+----------------------+ |...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: --------------------------------------+ | NVIDIA-SMI 525.60.13 Driver Version: 525.60.13 CUDA Version: 12.0 | |-------------------------------+----------------------+----------------------+ | GPU Name Persistence-M| Bus...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: In k8s pod, it takes approximately 1 hour to start the model using vllm bug ### Your current environment ### python 3.10.14 ### GPU is V100 * 4 ### nvidia-smi ``` Thu Jul 11 10:53:42 2024 +-----------------------...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: 4.66.4 transformers 4.41.0 triton 2.3.0 typer 0.11.1 typing_extensions 4.12.1 typing-inspect 0.9.0 tzdata 2024.1 ujson
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: 2024.1 PyYAML 6.0.1 quantile-python 1.1 ray 2.23.0 referencing 0.35.1 regex 2024.5.15 requests 2.32.3 rich
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: current environment ### python 3.10.14 ### GPU is V100 * 4 ### nvidia-smi ``` Thu Jul 11 10:53:42 2024 +-----------------------------------------------------------------------------+ | NVIDIA-SMI 525.60.13 Driver Versio...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
