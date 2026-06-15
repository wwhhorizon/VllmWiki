# vllm-project/vllm#1188: Task finished unexpectedly. when run a wizardcode request

| 字段 | 值 |
| --- | --- |
| Issue | [#1188](https://github.com/vllm-project/vllm/issues/1188) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;moe;quantization;sampling |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Task finished unexpectedly. when run a wizardcode request

### Issue 正文摘录

**GPU ENV:** +-----------------------------------------------------------------------------+ | NVIDIA-SMI 450.102.04 Driver Version: 450.102.04 CUDA Version: 11.0 | |-------------------------------+----------------------+----------------------+ | GPU Name Persistence-M| Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap| Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |===============================+======================+======================| | 0 Tesla V100-SXM2... On | 00000000:00:09.0 Off | 0 | | N/A 32C P0 37W / 300W | 31573MiB / 32510MiB | 0% Default | | | | N/A | +-------------------------------+----------------------+----------------------+ +-----------------------------------------------------------------------------+ | Processes: | | GPU GI CI PID Type Process name GPU Memory | | ID ID Usage | |=============================================================================| | 0 N/A N/A 3406559 C python 31561MiB | +-----------------------------------------------------------------------------+ **start command** :(base) [root@VM-114-86-tencentos ~]# python -m vllm.entrypoints.api_server --model WizardLM/WizardCoder-Python-13B-V1.0 --gpu-memory-utilizat...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: --------------------------------------+ | NVIDIA-SMI 450.102.04 Driver Version: 450.102.04 CUDA Version: 11.0 | |-------------------------------+----------------------+----------------------+ | GPU Name Persistence-M| B...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: --------------------------------------------------------------+ | NVIDIA-SMI 450.102.04 Driver Version: 450.102.04 CUDA Version: 11.0 | |-------------------------------+----------------------+----------------------+ | G...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ode((uint8)(cursor), cursorLen, newpos)\n\t\t\t\tcursorLen = 1\n\t\t\t} else {\n\t\t\t\tcursorLen++\n\t\t\t}\n\t\t\tcursor = 0\n\t\t} else if idxV == 0xff {\n\t\t\t// 新值为连续1\n\t\t\tif cursor == 0 {\n\t\t\t\t// 尾端为连续的0,...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: st d3ec023c4cab40299a715adf331ac01d: prompt: 'You are an AI unit testing expert. Your task is to help users write high-quality unit test cases by providing guidance on best practices, such as test coverage, test indepen...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ` performance attention_kv_cache;ci_build;frontend_api;model_support;moe;quantization;sampling_logits;scheduler_memory cache;cuda;moe;quantization;sampling crash;slowdown dtype;env_dependency **GPU ENV:**

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
