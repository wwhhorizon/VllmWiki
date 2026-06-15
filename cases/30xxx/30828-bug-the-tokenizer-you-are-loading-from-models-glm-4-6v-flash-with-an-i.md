# vllm-project/vllm#30828: [Bug]: The tokenizer you are loading from '/models/GLM-4.6V-Flash' with an incorrect regex pattern: https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503/discussions/84#69121093e8b480e709447d5e. This will lead to incorrect tokenization.

| 字段 | 值 |
| --- | --- |
| Issue | [#30828](https://github.com/vllm-project/vllm/issues/30828) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization |
| 症状 | crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The tokenizer you are loading from '/models/GLM-4.6V-Flash' with an incorrect regex pattern: https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503/discussions/84#69121093e8b480e709447d5e. This will lead to incorrect tokenization.

### Issue 正文摘录

### Your current environment ` root@node37:/disk1/GLM-4.6V-Flash# vi docker-compose.yml services: # vllm vllm-openai: image: vllm/vllm-openai:v0.12.0 container_name: GLM-4.6V-Flash restart: unless-stopped runtime: nvidia ports: - 8035:8000 volumes: - /disk1/:/models command: > --model /models/GLM-4.6V-Flash --tokenizer_mode="auto" --dtype=bfloat16 --tensor_parallel_size=1 --gpu-memory-utilization=0.8 --max-model-len=32768 --max_num_seqs=256 --served-model-name=GLM-4.6V-Flash deploy: resources: reservations: devices: - driver: nvidia capabilities: [gpu] device_ids: [ "0" ] ipc: host networks: vllm: ~ "docker-compose.yml" [dos] 30L, 722C written root@node37:/disk1/GLM-4.6V-Flash# docker compose down root@node37:/disk1/GLM-4.6V-Flash# docker compose up -d [+] Running 2/2 ✔ Network glm-46v-flash_default Created 0.1s ✔ Container GLM-4.6V-Flash Started 3.1s root@node37:/disk1/GLM-4.6V-Flash# docker logs -f GLM-4.6V-Flash WARNING 12-16 17:41:09 [argparse_utils.py:195] With `vllm serve`, you should provide the model as a positional argument or in a config file instead of via the `--model` option. The `--model` option will be removed in v0.13. (APIServer pid=1) INFO 12-16 17:41:09 [api_ser...

## 现有链接修复摘要

#30845 [ROCm] Group quant RMS norm fusion patterns

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: The tokenizer you are loading from '/models/GLM-4.6V-Flash' with an incorrect regex pattern: https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503/discussions/84#69121093e8b480e709447d5e. This will...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: le ### Your current environment ` root@node37:/disk1/GLM-4.6V-Flash# vi docker-compose.yml services: # vllm vllm-openai: image: vllm/vllm-openai:v0.12.0 container_name: GLM-4.6V-Flash restart: unless-stopped runtime: nv...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: --model /models/GLM-4.6V-Flash --tokenizer_mode="auto" --dtype=bfloat16 --tensor_parallel_size=1 --gpu-memory-utilization=0.8 --max-model-len=32768 --max_num_seqs=256 --served-model-name=GLM-4.6V-Flash deploy: resources...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ith an incorrect regex pattern: https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503/discussions/84#69121093e8b480e709447d5e. This will lead to incorrect tokenization. bug;stale ### Your current environm...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: #69121093e8b480e709447d5e. This will lead to incorrect tokenization. bug;stale ### Your current environment ` root@node37:/disk1/GLM-4.6V-Flash# vi docker-compose.yml services: # vllm vllm-openai: image: vllm/vllm-opena...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#30845](https://github.com/vllm-project/vllm/pull/30845) | mentioned | 0.6 |  [ROCm] Group quant RMS norm fusion patterns | [ROCm] Group quant RMS norm fusion patterns ## Purpose #30828 Guards creation of group quant patterns with current_platform.is_cuda() as a quick patch for ROCm platform. T |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
