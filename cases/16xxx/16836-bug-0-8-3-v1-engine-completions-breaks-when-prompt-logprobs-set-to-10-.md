# vllm-project/vllm#16836: [Bug]: 0.8.3 V1 engine /completions breaks when prompt_logprobs set to 10; works when set between 1-9

| 字段 | 值 |
| --- | --- |
| Issue | [#16836](https://github.com/vllm-project/vllm/issues/16836) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: 0.8.3 V1 engine /completions breaks when prompt_logprobs set to 10; works when set between 1-9

### Issue 正文摘录

### Your current environment 4xA100 ``` docker volume create HF docker run -d --rm --shm-size=100g --name llm_server -v HF:/app/cache -e VLLM_USE_V1=1 -e HF_HOME=/app/cache -e HF_HUB_CACHE=/app/cache/hub -e VLLM_LOGGING_LEVEL=DEBUG --gpus 0 --runtime=nvidia -p 6919:6919 --network comm vllm/vllm-openai:v0.8.3 --model casperhansen/deepseek-r1-distill-qwen-32b-awq --tokenizer casperhansen/deepseek-r1-distill-qwen-32b-awq --dtype float16 --max_model_len 16000 --gpu_memory_utilization 0.7 --tensor-parallel-size 1 --num-scheduler-steps 1 --port 6919 --enable-chunked-prefill --dtype half ``` using input to /completions: ``` { "prompt": "In contrast, the rule asproposed would have required sources to document for each processall major hazards, the consequences of each of these hazards, therisk reduction steps taken to address each hazard, and theconsequences of each risk reduction step Both changes signal a stripping down, an oldman's effort to simplify, relearn, restart The zeitgeist contends that an aquarius of the discussion is assumed to be an inmost chair. Before radios, jails were only appeals. The bareback microwave comes from a fulgid effect. A feedback can hardly be considered a...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: bug;stale ### Your current environment 4xA100 ``` docker volume create HF docker run -d --rm --shm-size=100g --name llm_server -v HF:/app/cache -e VLLM_USE_V1=1 -e HF_HOME=/app/cache -e HF_HUB_CACHE=/app/cache/hub -e VL...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: qwen-32b-awq --tokenizer casperhansen/deepseek-r1-distill-qwen-32b-awq --dtype float16 --max_model_len 16000 --gpu_memory_utilization 0.7 --tensor-parallel-size 1 --num-scheduler-steps 1 --port 6919 --enable-chunked-pre...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 10; works when set between 1-9 bug;stale ### Your current environment 4xA100 ``` docker volume create HF docker run -d --rm --shm-size=100g --name llm_server -v HF:/app/cache -e VLLM_USE_V1=1 -e HF_HOME=/app/cache -e HF...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ore stevens, stamps were only mini-skirts. Nowhere is it disputed that a block is an unthought kite. A clinical research guide fortherapists treating individuals with alcohol abuse and dependence 6 With a lockstitch mac...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ns breaks when prompt_logprobs set to 10; works when set between 1-9 bug;stale ### Your current environment 4xA100 ``` docker volume create HF docker run -d --rm --shm-size=100g --name llm_server -v HF:/app/cache -e VLL...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
