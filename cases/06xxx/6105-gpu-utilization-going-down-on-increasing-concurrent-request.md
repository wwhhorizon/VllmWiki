# vllm-project/vllm#6105: GPU utilization going down on increasing concurrent request  

| 字段 | 值 |
| --- | --- |
| Issue | [#6105](https://github.com/vllm-project/vllm/issues/6105) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;model_support |
| 子分类 | precision |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> GPU utilization going down on increasing concurrent request  

### Issue 正文摘录

### Your current environment - vLLM openai docker image: v0.3.2 - Nvidia A100 GPU - Nvidia Cuda Toolkit: 12.2 ### 🐛 Describe the bug As the number of concurrent requests increases, GPU utilization is expected to rise. However, GPU utilization is decreasing as the number of concurrent requests grows. The vLLM server, loaded with the Llama 2 model using float16 precision on an Nvidia GPU, shows a decrease in GPU utilization from 94% to 56% when concurrent requests increase from 1 to 100. Apache bench is used for load testing the server. ```sh docker run --runtime nvidia --gpus all \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --env "HUGGING_FACE_HUB_TOKEN= " \ -p 8000:8000 \ --shm_size 16G \ vllm/vllm-openai:v0.3.2 \ --model meta-llama/Llama-2-7b-chat-hf --dtype float16 ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: he number of concurrent requests grows. The vLLM server, loaded with the Llama 2 model using float16 precision on an Nvidia GPU, shows a decrease in GPU utilization from 94% to 56% when concurrent requests increase from...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ncurrent request bug;stale ### Your current environment - vLLM openai docker image: v0.3.2 - Nvidia A100 GPU - Nvidia Cuda Toolkit: 12.2 ### 🐛 Describe the bug As the number of concurrent requests increases, GPU utiliza...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ent requests grows. The vLLM server, loaded with the Llama 2 model using float16 precision on an Nvidia GPU, shows a decrease in GPU utilization from 94% to 56% when concurrent requests increase from 1 to 100. Apache be...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ## Your current environment - vLLM openai docker image: v0.3.2 - Nvidia A100 GPU - Nvidia Cuda Toolkit: 12.2 ### 🐛 Describe the bug As the number of concurrent requests increases, GPU utilization is expected to rise. Ho...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: GPU utilization going down on increasing concurrent request bug;stale ### Your current environment - vLLM openai docker image: v0.3.2 - Nvidia A100 GPU - Nvidia Cuda Toolkit: 12.2 ### 🐛 Describe the bug As the number of...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
