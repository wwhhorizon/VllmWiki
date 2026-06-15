# vllm-project/vllm#4195: [Bug]: undefined symbol: ncclcommregister when run docker built from the latest source code 

| 字段 | 值 |
| --- | --- |
| Issue | [#4195](https://github.com/vllm-project/vllm/issues/4195) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: undefined symbol: ncclcommregister when run docker built from the latest source code 

### Issue 正文摘录

### Your current environment We tested in tow environments, environment info in bellow. ### 🐛 Describe the bug We built a docker image from the latest source code (2024/04/18), to run CohereForAI/c4ai-command-r-plus. We test in two environment: ### First environment Everything works fine, we use A100 machine, and output of `collect_env.py`: ``` 4pdvGPU Msg(682:140318609781760:libvgpu.c:869)]: Initializing..... [4pdvGPU Warn(682:140318609781760:hook.c:475)]: remap handles for device 0 /usr/lib/python3.10/runpy.py:126: RuntimeWarning: 'torch.utils.collect_env' found in sys.modules after import of package 'torch.utils', but prior to execution of 'torch.utils.collect_env'; this may result in unpredictable behaviour warn(RuntimeWarning(msg)) Collecting environment information... [4pdvGPU Warn(682:140318609781760:utils.c:228)]: get default cuda 1 from (null) [4pdvGPU Msg(682:140318609781760:libvgpu.c:902)]: Initialized PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.29.2 Libc versi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Bug]: undefined symbol: ncclcommregister when run docker built from the latest source code bug ### Your current environment We tested in tow environments, environment info in bellow. ### 🐛 Describe the bug We built a d...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: n two environment: ### First environment Everything works fine, we use A100 machine, and output of `collect_env.py`: ``` 4pdvGPU Msg(682:140318609781760:libvgpu.c:869)]: Initializing..... [4pdvGPU Warn(682:1403186097817...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: edictable behaviour warn(RuntimeWarning(msg)) Collecting environment information... [4pdvGPU Warn(682:140318609781760:utils.c:228)]: get default cuda 1 from (null) [4pdvGPU Msg(682:140318609781760:libvgpu.c:902)]: Initi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: the command ```python python3 -m vllm.entrypoints.openai.api_server --dtype half --model /root/.cache/LLM-Repo/model/c4ai-command-r-plus-GPTQ --trust-remote-code ``` shows the following error: ![img_v3_02a3_5b2b95af-546...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT vulnerable Vulnerability Retbleed: Not affected Vulnerability Spec store bypass: Mitigation; Speculative Store...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
