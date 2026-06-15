# vllm-project/vllm#25653: [Bug]:  AttributeError: MoE Model GptOssForCausalLM does not support BitsAndBytes quantization yet.

| 字段 | 值 |
| --- | --- |
| Issue | [#25653](https://github.com/vllm-project/vllm/issues/25653) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;moe;operator;quantization;sampling |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  AttributeError: MoE Model GptOssForCausalLM does not support BitsAndBytes quantization yet.

### Issue 正文摘录

### Your current environment docker 0.10.2rc3.dev371+g5774b0a1d ### 🐛 Describe the bug GPU 2080 MAX-Q Windows 11 PS D:\model\llama\llama-b6529-bin-win-cuda-12.4-x64> docker run --runtime nvidia --gpus all -v D:/model:/root/model -p 8000:8000 --ipc=host vllm/vllm-openai:nightly --model /root/model/gpt-oss-20b-unsloth-bnb-4bit /usr/local/lib/python3.12/dist-packages/torch/cuda/__init__.py:63: FutureWarning: The pynvml package is deprecated. Please install nvidia-ml-py instead. If you did not install pynvml directly, please report this to the maintainers of the package that installed pynvml for you. import pynvml # type: ignore[import] INFO 09-25 01:26:39 [__init__.py:216] Automatically detected platform cuda. (APIServer pid=1) INFO 09-25 01:26:42 [api_server.py:1822] vLLM API server version 0.10.2rc3.dev371+g5774b0a1d (APIServer pid=1) INFO 09-25 01:26:42 [utils.py:328] non-default args: {'model': '/root/model/gpt-oss-20b-unsloth-bnb-4bit'} (APIServer pid=1) INFO 09-25 01:26:52 [model.py:550] Resolved architecture: GptOssForCausalLM (APIServer pid=1) `torch_dtype` is deprecated! Use `dtype` instead! (APIServer pid=1) INFO 09-25 01:26:52 [model.py:1576] Using max model len 131072 (AP...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: t BitsAndBytes quantization yet. bug;stale ### Your current environment docker 0.10.2rc3.dev371+g5774b0a1d ### 🐛 Describe the bug GPU 2080 MAX-Q Windows 11 PS D:\model\llama\llama-b6529-bin-win-cuda-12.4-x64> docker run...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: AttributeError: MoE Model GptOssForCausalLM does not support BitsAndBytes quantization yet. bug;stale ### Your current environment docker 0.10.2rc3.dev371+g5774b0a1d ### 🐛 Describe the bug GPU 2080 MAX-Q Windows...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: el GptOssForCausalLM does not support BitsAndBytes quantization yet. bug;stale ### Your current environment docker 0.10.2rc3.dev371+g5774b0a1d ### 🐛 Describe the bug GPU 2080 MAX-Q Windows 11 PS D:\model\llama\llama-b65...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ttributeError: MoE Model GptOssForCausalLM does not support BitsAndBytes quantization yet. bug;stale ### Your current environment docker 0.10.2rc3.dev371+g5774b0a1d ### 🐛 Describe the bug GPU 2080 MAX-Q Windows 11 PS D:...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: [Bug]: AttributeError: MoE Model GptOssForCausalLM does not support BitsAndBytes quantization yet. bug;stale ### Your current environment docker 0.10.2rc3.dev371+g5774b0a1d ### 🐛 Describe the bug GPU 2080 MAX-Q Windows...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
