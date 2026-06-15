# vllm-project/vllm#8938: [Bug]: --served-model-name doesn't work with OpenAI benchmarking script

| 字段 | 值 |
| --- | --- |
| Issue | [#8938](https://github.com/vllm-project/vllm/issues/8938) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: --served-model-name doesn't work with OpenAI benchmarking script

### Issue 正文摘录

update: I think I may be able to get it to work by providing a separate --tokenizer. Confirmed, this is solved by using --tokenizer: ``` python3 benchmark_serving.py --backend openai \ --base-url http://127.0.0.1:8000/openai/ \ --dataset-name=random \ --model meta-llama-3.2-11b-vision-instruct \ --seed 12345 --tokenizer neuralmagic/Llama-3.2-11B-Vision-Instruct-FP8-dynamic ``` ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I can reproduce this when using vLLM OpenAI endpoint using the following args: ``` --served-model-name=meta-llama-3.2-11b-vision-instruct ``` root cause, the benchmarking script tries to validate the model in huggingface, but it should not do that because model name does not always have to be a valid HF model. The model name can be tweaked by using --served-model-name. I plan to make a PR to tackle this. Afterwards run the benchmarking script: ``` python3 benchmark_serving.py --backend openai \ --base-url http://127.0.0.1:8000/openai/ \ --dataset-name=random \ --model meta-llama-3.2-11b-vision-instruct \ --seed 12345 None of PyTorch, TensorFlow >= 2.0, or Flax have been found. Models won't be available and only tokenizers...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: --served-model-name doesn't work with OpenAI benchmarking script bug update: I think I may be able to get it to work by providing a separate --tokenizer. Confirmed, this is solved by using --tokenizer: ``` python...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: --served-model-name doesn't work with OpenAI benchmarking script bug update: I think I may be able to get it to work by providing a separate --tokenizer. Confirmed, this is solved by using --tokenizer: ``` python...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ion-instruct/resolve/main/tokenizer_config.json. Please make sure you specified the correct `repo_id` and `repo_type`. If you are trying to access a private or gated repo, make sure you are authenticated. The above exce...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: \ --seed 12345 --tokenizer neuralmagic/Llama-3.2-11B-Vision-Instruct-FP8-dynamic ``` ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I can reproduce this when using vLLM OpenAI en...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: this is solved by using --tokenizer: ``` python3 benchmark_serving.py --backend openai \ --base-url http://127.0.0.1:8000/openai/ \ --dataset-name=random \ --model meta-llama-3.2-11b-vision-instruct \ --seed 12345 --tok...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
