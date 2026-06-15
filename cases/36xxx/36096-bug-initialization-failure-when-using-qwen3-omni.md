# vllm-project/vllm#36096: [Bug]: Initialization failure when using Qwen3-Omni

| 字段 | 值 |
| --- | --- |
| Issue | [#36096](https://github.com/vllm-project/vllm/issues/36096) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | cuda;gemm;operator;quantization |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Initialization failure when using Qwen3-Omni

### Issue 正文摘录

### Your current environment Couldnt get collect_env.py to work properly on NixOS ### 🐛 Describe the bug When I run the following command, i hit a "Engine core initialization failed" ```sh $ vllm serve Qwen/Qwen3-Omni-30B-A3B-Instruct ``` The logs mention: ```text (EngineCore_DP0 pid=834284) File "/nix/store/ds2cd60bkb0mpg99ph241ak804z9zgh6-python3.13-transformers-5.2.0/lib/python3.13/site-packages/transformers/models/qwen2_vl/image_processing_qwen2_vl.py", line 92, in smart_resize (EngineCore_DP0 pid=834284) if h_bar * w_bar > max_pixels: (EngineCore_DP0 pid=834284) ^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=834284) TypeError: '>' not supported between instances of 'int' and 'NoneType' ``` So I tried passing the max_pixels like ```sh $ vllm serve cyankiwi/Qwen3-Omni-30B-A3B-Instruct-AWQ-4bit --mm-processor-kwargs.max_pixels 1003520 $ vllm serve cyankiwi/Qwen3-Omni-30B-A3B-Instruct-AWQ-4bit --mm-processor-kwargs '{"max_pixels": 1003520}' ``` but neither had an effect. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/),...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Initialization failure when using Qwen3-Omni bug ### Your current environment Couldnt get collect_env.py to work properly on NixOS ### 🐛 Describe the bug When I run the following command, i hit a "Engine core ini...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization;scheduler_memory cuda;gemm;operator;quantization crash;sl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: /transformers/models/qwen2_vl/image_processing_qwen2_vl.py", line 92, in smart_resize (EngineCore_DP0 pid=834284) if h_bar * w_bar > max_pixels: (EngineCore_DP0 pid=834284) ^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: build;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization;scheduler_memory cuda;gemm;operator;quantization crash;slowdown dtype;env_dependency Your current environment
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ns. performance ci_build;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization;scheduler_memory cuda;gemm;operator;quantization crash;slowdown dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
