# vllm-project/vllm#17396: [Bug]: The size of tensor a (49472) must match the size of tensor b (49664) at non-singleton dimension 1

| 字段 | 值 |
| --- | --- |
| Issue | [#17396](https://github.com/vllm-project/vllm/issues/17396) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: The size of tensor a (49472) must match the size of tensor b (49664) at non-singleton dimension 1

### Issue 正文摘录

### Your current environment I'm trying to use a lora adapter along its base model on my CPUs only machine from a docker container. I first build a local cpu based image, like below: ``` git checkout v0.8.5 docker build -f docker/Dockerfile.cpu -t vllm-0.8.5-cpu-env --shm-size=4g . ``` From there, I'm able to run the model and associated lora adapter with success: ``` docker run -it --mount type=bind,source=/home/agallice/dev/hugging-face-models/,target=/hf-models --rm --network=host vllm-0.8.4-cpu-env --model /hf-models/granite-3.2-8b-instruct --max-model-len 16384 --enable-lora --lora-modules uncertainty-lora=/hf-models/granite-uncertainty-3.2-8b-lora ``` However, this all break on the first request, even simply requesting the base model ala below: ``` [main_upstream @ uncertainty-quarkus-experiments]$ curl -X POST "http://localhost:8000/v1/chat/completions" \ -H "Content-Type: application/json" \ --data '{ "model": "/hf-models/granite-3.2-8b-instruct", "messages": [ { "role": "user", "content": "What is the capital of France?" } ] }' ``` The served engine crashes with below stack trace: I've tried to experiment with different setups, command line arguments and so on. To no avai...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: o use a lora adapter along its base model on my CPUs only machine from a docker container. I first build a local cpu based image, like below: ``` git checkout v0.8.5 docker build -f docker/Dockerfile.cpu -t vllm-0.8.5-c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: our current environment I'm trying to use a lora adapter along its base model on my CPUs only machine from a docker container. I first build a local cpu based image, like below: ``` git checkout v0.8.5 docker build -f d...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ranite-uncertainty-3.2-8b-lora ``` However, this all break on the first request, even simply requesting the base model ala below: ``` [main_upstream @ uncertainty-quarkus-experiments]$ curl -X POST "http://localhost:800...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
