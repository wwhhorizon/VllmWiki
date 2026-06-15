# vllm-project/vllm#2247: Running from Docker with Local Model Files Failed

| 字段 | 值 |
| --- | --- |
| Issue | [#2247](https://github.com/vllm-project/vllm/issues/2247) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Running from Docker with Local Model Files Failed

### Issue 正文摘录

I tried to run vllm from Docker image follow the official tutorial https://docs.vllm.ai/en/latest/serving/deploying_with_docker.html. My model files are stored at `/home/appuser/repo/models/Qwen-14b-Chat-AWQ`, I launched the docker image with command: `docker run --gpus all -v /home/appuser/repo/models:/root/.cache/huggingface -p 8800:8000 --ipc=host vllm/vllm-openai:latest --model Qwen-14B-Chat-AWQ --quantization awq --tensor-parallel-size 2`, however, vllm reported it failed to load the model file: ``` OSError: We couldn't connect to 'https://huggingface.co' to load this file, couldn't find it in the cached files and it looks like Qwen-14B-Chat-AWQ is not the path to a directory containing a file named config.json. ``` Then, I looked into the image, ``` docker run --rm -it -v /home/appuser/repo/models:/root/.cache/huggingface --entrypoint bash vllm/vllm-openai:latest ls /root/.cache/huggingface/ Qwen-14B-Chat-AWQ ``` Obviously, the model folder is right there. Can anyone tell how to mount local model files into vllm docker image?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Running from Docker with Local Model Files Failed I tried to run vllm from Docker image follow the official tutorial https://docs.vllm.ai/en/latest/serving/deploying_with_docker.html. My model files are stored at `/home...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Running from Docker with Local Model Files Failed I tried to run vllm from Docker image follow the official tutorial https://docs.vllm.ai/en/latest/serving/deploying_with_docker.html. My model files are stored at `/home...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: 8800:8000 --ipc=host vllm/vllm-openai:latest --model Qwen-14B-Chat-AWQ --quantization awq --tensor-parallel-size 2`, however, vllm reported it failed to load the model file: ``` OSError: We couldn't connect to 'https://...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: from Docker image follow the official tutorial https://docs.vllm.ai/en/latest/serving/deploying_with_docker.html. My model files are stored at `/home/appuser/repo/models/Qwen-14b-Chat-AWQ`, I launched the docker image w...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
