# vllm-project/vllm#15845: [Bug]: served-model-name not being returned in model field of response

| 字段 | 值 |
| --- | --- |
| Issue | [#15845](https://github.com/vllm-project/vllm/issues/15845) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: served-model-name not being returned in model field of response

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I might be confused about how all of this works so sorry if this isn't a bug but I figured I'd post what I'm seeing. I recently upgraded vLLM from 0.6.6 to 0.8.2 and have had some trouble with the `served-model-name` parameter. It doesn't seem like it's being honored in the response. [From the docs](https://docs.vllm.ai/en/latest/serving/engine_args.html#:~:text=The%20model%20name%20in%20the%20model%20field%20of%20a%20response%20will%20be%20the%20first%20name%20in%20this%20list.), it sounds like the model name in the model field of a response will be the first name in this list. However when I run: ```bash VLLM_USE_CUDA=0 python -m vllm.entrypoints.openai.api_server \ --model TinyLlama/TinyLlama-1.1B-Chat-v1.0 \ --tensor-parallel-size 1 \ --host 0.0.0.0 \ --port 8000 \ --dtype float16 \ --served-model-name finetune-test TinyLlama/TinyLlama-1.1B-Chat-v1.0 ``` And call the API with: ```python import requests import json # change for your host VLLM_HOST = "http://0.0.0.0:8000" url = f"{VLLM_HOST}/v1/completions" headers = {"Content-Type": "application/json"} data = { "model": "TinyLlama/TinyLlama-1.1B-Chat-v1.0", "prompt": "JupySQL...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: inyLlama/TinyLlama-1.1B-Chat-v1.0 ``` And call the API with: ```python import requests import json # change for your host VLLM_HOST = "http://0.0.0.0:8000" url = f"{VLLM_HOST}/v1/completions" headers = {"Content-Type":...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: served-model-name not being returned in model field of response bug;stale ### Your current environment ### 🐛 Describe the bug I might be confused about how all of this works so sorry if this isn't a bug but I fig...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: --tensor-parallel-size 1 \ --host 0.0.0.0 \ --port 8000 \ --dtype float16 \ --served-model-name finetune-test TinyLlama/TinyLlama-1.1B-Chat-v1.0 ``` And call the API with: ```python import requests import json # change...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: l be the first name in this list. However when I run: ```bash VLLM_USE_CUDA=0 python -m vllm.entrypoints.openai.api_server \ --model TinyLlama/TinyLlama-1.1B-Chat-v1.0 \ --tensor-parallel-size 1 \ --host 0.0.0.0 \ --por...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ug]: served-model-name not being returned in model field of response bug;stale ### Your current environment ### 🐛 Describe the bug I might be confused about how all of this works so sorry if this isn't a bug but I figur...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
