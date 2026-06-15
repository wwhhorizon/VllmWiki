# vllm-project/vllm#20193: [Bug]: Blackwell, no kernel image is available for execution on the device

| 字段 | 值 |
| --- | --- |
| Issue | [#20193](https://github.com/vllm-project/vllm/issues/20193) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Blackwell, no kernel image is available for execution on the device

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi there. I cant get VLLM to work with cuda no matter what i do. Running on a 5080 mobile. Installed everything on a new virtual environment, python 3.10. I have tried running qwen 8b and 0.6b fp8 (with quantization set as fp8). It takes a long time to load and hangs When I try 14b-awq (quantization = "awq_marlin") it fails with this error: ``` Fetching 12 files: 100%|██████████| 12/12 [00:00 ", line 81, in [rank0]: File "/home/tomwright/PycharmProjects/vllm_try/venv/lib/python3.12/site-packages/vllm/entrypoints/llm.py", line 243, in __init__ [rank0]: self.llm_engine = LLMEngine.from_engine_args( [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/home/tomwright/PycharmProjects/vllm_try/venv/lib/python3.12/site-packages/vllm/engine/llm_engine.py", line 501, in from_engine_args [rank0]: return engine_cls.from_vllm_config( [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/home/tomwright/PycharmProjects/vllm_try/venv/lib/python3.12/site-packages/vllm/engine/llm_engine.py", line 477, in from_vllm_config [rank0]: return cls( [rank0]: ^^^^ [rank0]: File "/home/tomwright/PycharmProjects/vllm_try/venv/lib/python3.12/site-packages/vl...

## 现有链接修复摘要

#21077 [Bugfix] Voxtral on Blackwell GPUs (RTX 50 series)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: VLLM to work with cuda no matter what i do. Running on a 5080 mobile. Installed everything on a new virtual environment, python 3.10. I have tried running qwen 8b and 0.6b fp8 (with quantization set as fp8). It takes a...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: irtual environment, python 3.10. I have tried running qwen 8b and 0.6b fp8 (with quantization set as fp8). It takes a long time to load and hangs When I try 14b-awq (quantization = "awq_marlin") it fails with this error...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: rything on a new virtual environment, python 3.10. I have tried running qwen 8b and 0.6b fp8 (with quantization set as fp8). It takes a long time to load and hangs When I try 14b-awq (quantization = "awq_marlin") it fai...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Blackwell, no kernel image is available for execution on the device bug;stale ### Your current environment ### 🐛 Describe the bug Hi there. I cant get VLLM to work with cuda no matter what i do. Running on a 508
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: wright/PycharmProjects/bertopcing/test.xlsx") os.environ['VLLM_ATTENTION_BACKEND']="FLASHINFER" os.environ['VLLM_USE_V1'] = "0" doc_ls = [] # Filter out Topic -1 and group by "Topic" grouped_topics = tmp[tmp["Topic"] !=...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#21077](https://github.com/vllm-project/vllm/pull/21077) | mentioned | 0.6 | [Bugfix] Voxtral on Blackwell GPUs (RTX 50 series) | end for compatibility Similar PR: #20998 Similar Issues: #20025, #20193 ## Test Plan Use the command from Mistral AI documentation to start a server ```bash uv run vllm serve mist |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
