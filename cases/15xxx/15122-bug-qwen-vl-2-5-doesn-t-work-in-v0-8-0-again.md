# vllm-project/vllm#15122: [Bug]: Qwen VL 2.5 doesn't work in v0.8.0 - again

| 字段 | 值 |
| --- | --- |
| Issue | [#15122](https://github.com/vllm-project/vllm/issues/15122) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support;multimodal_vlm |
| 子分类 | kernel_eff |
| Operator 关键词 | gemm |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen VL 2.5 doesn't work in v0.8.0 - again

### Issue 正文摘录

### Your current environment Official docker container v0.8.0 from https://hub.docker.com/r/vllm/vllm-openai/tags Setup with something like ``` services: vllm-qwen25-vl-72b: image: vllm/vllm-openai:v0.8.0 container_name: vllm-qwen25-vl-72b environment: - HF_TOKEN=$HF_TOKEN - VLLM_NO_USAGE_STATS=1 ipc: host deploy: resources: reservations: devices: - driver: nvidia device_ids: ['0', '1', '2', '3'] capabilities: [ gpu ] network_mode: host volumes: - /mnt/sda/huggingface:/root/.cache/huggingface - .:/opt/vllm command: - --port=8003 - --model=Qwen/Qwen2.5-VL-72B-Instruct - --tensor-parallel-size=4 - --limit-mm-per-prompt=image=2 - --disable-log-requests - --gpu-memory-utilization=0.90 - --swap-space=5 restart: unless-stopped ``` ### 🐛 Describe the bug The images are all totally wrong or partially wrong. Example call: ``` curl 'https://ai1.dev.init/llm-vision/v1/chat/completions' -k -H 'Content-Type: application/json' -d @- <<EOF { "model": "Qwen/Qwen2.5-VL-72B-Instruct", "messages": [ { "role": "user", "content": [ { "type": "image_url", "image_url": { "url": "data:image/avif;base64,$(curl -s https://aomediacodec.github.io/av1-avif/testFiles/Link-U/hato.jpg | base64 -w 0)" } }, { "typ...

## 现有链接修复摘要

#15200 [Bugfix] Fix incorrect qwen2.5-vl attention mask pre-computation

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: 2.5 doesn't work in v0.8.0 - again bug ### Your current environment Official docker container v0.8.0 from https://hub.docker.com/r/vllm/vllm-openai/tags Setup with something like ``` services: vllm-qwen25-vl-72b: image:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Qwen VL 2.5 doesn't work in v0.8.0 - again bug ### Your current environment Official docker container v0.8.0 from https://hub.docker.com/r/vllm/vllm-openai/tags Setup with something like ``` services: vllm-qwen25...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 5 72, which is normally very very good. Something is wrong. Do you have small automatic tests/benchmarks for some base models, if you make sweeping arch/design changes and very commonly used models don't run over multip...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: data:image/avif;base64,$(curl -s https://aomediacodec.github.io/av1-avif/testFiles/Link-U/hato.jpg | base64 -w 0)" } }, { "type": "text", "text": "Describe image" } ]
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: } ] } ], "skip_special_tokens": false } EOF ``` Result: ``` {"id":"chatcmpl-5e74576b1fb64899a05658b15968a549","object":"chat.completion","created":1742382493,"model":"Qwen/Qwen2-VL-7B-Instruct","choices":[{"index":0,"me...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#15200](https://github.com/vllm-project/vllm/pull/15200) | closes_keyword | 0.95 | [Bugfix] Fix incorrect qwen2.5-vl attention mask pre-computation | FIX #15122 FIX #15197 - Fix incorrect attention mask creation for qwen2.5-vl windows attention from #14377 <!--- pyml disable-next-line no-emphasis-as-heading --> |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
