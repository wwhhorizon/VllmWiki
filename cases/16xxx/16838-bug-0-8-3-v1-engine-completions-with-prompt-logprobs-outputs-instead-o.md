# vllm-project/vllm#16838: [Bug]: 0.8.3 V1 engine /completions with prompt_logprobs outputs `Ġ` instead of a space ` ` in `decoded_token`

| 字段 | 值 |
| --- | --- |
| Issue | [#16838](https://github.com/vllm-project/vllm/issues/16838) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: 0.8.3 V1 engine /completions with prompt_logprobs outputs `Ġ` instead of a space ` ` in `decoded_token`

### Issue 正文摘录

### Your current environment 4xA100 ``` docker volume create HF docker run -d --rm --shm-size=100g --name llm_server -v HF:/app/cache -e VLLM_USE_V1=1 -e HF_HOME=/app/cache -e HF_HUB_CACHE=/app/cache/hub -e VLLM_LOGGING_LEVEL=DEBUG --gpus 0 --runtime=nvidia -p 6919:6919 --network comm vllm/vllm-openai:v0.8.3 --model casperhansen/deepseek-r1-distill-qwen-32b-awq --tokenizer casperhansen/deepseek-r1-distill-qwen-32b-awq --dtype float16 --max_model_len 16000 --gpu_memory_utilization 0.7 --tensor-parallel-size 1 --num-scheduler-steps 1 --port 6919 --enable-chunked-prefill --dtype half ``` experiment similar to other issue I raised #16836 ### 🐛 Describe the bug ``` { "prompt": "Acquisition of property, plant, and equipment throughexchange Arthur Campa believes that pachucos originated as a linguistic group first and had no distinctive dress style In particular,the women have been seized and burned as witches-all part of themale-supremacist purge of women's leadership in spreading the real,revolutionary93 news of the gospels Some posit the retuse rock to be less than audile. However, cabbages are choky appeals.A harbor is an enemy from the right perspective. This is not to discredit the...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: a space ` ` in `decoded_token` bug;stale ### Your current environment 4xA100 ``` docker volume create HF docker run -d --rm --shm-size=100g --name llm_server -v HF:/app/cache -e VLLM_USE_V1=1 -e HF_HOME=/app/cache -e HF...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: bug;stale ### Your current environment 4xA100 ``` docker volume create HF docker run -d --rm --shm-size=100g --name llm_server -v HF:/app/cache -e VLLM_USE_V1=1 -e HF_HOME=/app/cache -e HF_HUB_CACHE=/app/cache/hub -e VL...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: /completions with prompt_logprobs outputs `Ġ` instead of a space ` ` in `decoded_token` bug;stale ### Your current environment 4xA100 ``` docker volume create HF docker run -d --rm --shm-size=100g --name llm_server -v H...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ` in `decoded_token` bug;stale ### Your current environment 4xA100 ``` docker volume create HF docker run -d --rm --shm-size=100g --name llm_server -v HF:/app/cache -e VLLM_USE_V1=1 -e HF_HOME=/app/cache -e HF_HUB_CACHE...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: re is it disputed that few can name a pursued toast that isn't a dyeline block.We know that the literature would have us believe that an alate question is not but a loaf. The imprisonments could be said to resemble lent...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
