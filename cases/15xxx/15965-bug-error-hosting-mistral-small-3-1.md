# vllm-project/vllm#15965: [Bug]: Error hosting Mistral-Small-3.1

| 字段 | 值 |
| --- | --- |
| Issue | [#15965](https://github.com/vllm-project/vllm/issues/15965) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization;scheduler_memory |
| 子分类 | race_cond |
| Operator 关键词 | cuda;quantization;triton |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error hosting Mistral-Small-3.1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I installed the latest vllm using: pip install vllm --pre --extra-index-url https://wheels.vllm.ai/nightly --upgrade vllm-0.8.3.dev70+g4098b722 and host the model with: vllm serve mistralai/Mistral-Small-3.1-24B-Instruct-2503 --tokenizer_mode mistral --config_format mistral --load_format mistral --tool-call-parser mistral --enable-auto-tool-choice --limit_mm_per_prompt 'image=10' --tensor-parallel-size 2 But get error: /usr/lib/python3/dist-packages/scipy/init.py:146: UserWarning: A NumPy version >=1.17.3 and ={np_minversion} and ) Traceback (most recent call last): File "/home/ubuntu/.local/bin/vllm", line 8, in sys.exit(main()) File "/home/ubuntu/.local/lib/python3.10/site-packages/vllm/entrypoints/cli/main.py", line 75, in main args.dispatch_function(args) File "/home/ubuntu/.local/lib/python3.10/site-packages/vllm/entrypoints/cli/serve.py", line 33, in cmd uvloop.run(run_server(args)) File "/home/ubuntu/.local/lib/python3.10/site-packages/uvloop/init.py", line 82, in run return loop.run_until_complete(wrapper()) File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete File "/home/ubuntu/.local/lib/python3.10/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: Small-3.1 bug ### Your current environment ### 🐛 Describe the bug I installed the latest vllm using: pip install vllm --pre --extra-index-url https://wheels.vllm.ai/nightly --upgrade vllm-0.8.3.dev70+g4098b722 and host...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: eels.vllm.ai/nightly --upgrade vllm-0.8.3.dev70+g4098b722 and host the model with: vllm serve mistralai/Mistral-Small-3.1-24B-Instruct-2503 --tokenizer_mode mistral --config_format mistral --load_format mistral --tool-c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Error hosting Mistral-Small-3.1 bug ### Your current environment ### 🐛 Describe the bug I installed the latest vllm using: pip install vllm --pre --extra-index-url https://wheels.vllm.ai/nightly --upgrade vllm-0....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: n3.10/site-packages/vllm/entrypoints/cli/main.py", line 75, in main args.dispatch_function(args) File "/home/ubuntu/.local/lib/python3.10/site-packages/vllm/entrypoints/cli/serve.py", line 33, in cmd uvloop.run(run_serv...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization;scheduler_memory cuda;quantization;triton crash dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
