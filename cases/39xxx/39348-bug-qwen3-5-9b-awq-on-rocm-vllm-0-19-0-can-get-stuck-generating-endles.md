# vllm-project/vllm#39348: [Bug]: Qwen3.5-9B-AWQ on ROCm/vLLM 0.19.0 can get stuck generating endless "!" inside JSON schema output

| 字段 | 值 |
| --- | --- |
| Issue | [#39348](https://github.com/vllm-project/vllm/issues/39348) |
| 状态 | open |
| 标签 | bug;rocm |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | kernel_eff |
| Operator 关键词 | kernel;quantization;sampling |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | amd |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5-9B-AWQ on ROCm/vLLM 0.19.0 can get stuck generating endless "!" inside JSON schema output

### Issue 正文摘录

### Your current environment ### Environment details gathered locally ```text vLLM server version: 0.19.0 OS: PRETTY_NAME="Ubuntu 24.04.4 LTS" VERSION="24.04.4 LTS (Noble Numbat)" Kernel: Linux saturnix-AB350M-Pro4 6.17.0-20-generic #20~24.04.1-Ubuntu SMP PREEMPT_DYNAMIC Thu Mar 19 01:28:37 UTC 2 x86_64 x86_64 x86_64 GNU/Linux Python: Python 3.12.3 GPU: 09:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Navi 31 [Radeon RX 7900 XT/7900 XTX/7900 GRE/7900M] (rev cc) ROCm note from host: ROCk module is loaded Unable to open /dev/kfd read-write: No such file or directory saturnix is member of video group Model: QuantTrio/Qwen3.5-9B-AWQ Served model name: qwen3.5:9b Docker image: vllm/vllm-openai-rocm:latest Server launch command: sudo docker run --rm --network host \ --device /dev/kfd --device /dev/dri \ --group-add render \ --ipc=host --shm-size 16G \ -e PYTORCH_ALLOC_CONF=expandable_segments:True \ -v ~/.cache/huggingface:/root/.cache/huggingface \ vllm/vllm-openai-rocm:latest \ --model QuantTrio/Qwen3.5-9B-AWQ \ --served-model-name qwen3.5:9b \ --quantization awq \ --host 127.0.0.1 \ --port 11434 \ --max-model-len 16384 \ --enable-prefix-caching \ --max-num-se...

## 现有链接修复摘要

#20 Optimize data movement

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: vironment ### Environment details gathered locally ```text vLLM server version: 0.19.0 OS: PRETTY_NAME="Ubuntu 24.04.4 LTS" VERSION="24.04.4 LTS (Noble Numbat)" Kernel: Linux saturnix-AB350M-Pro4 6.17.0-20-generic #20~2...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen3.5-9B-AWQ on ROCm/vLLM 0.19.0 can get stuck generating endless "!" inside JSON schema output bug;rocm ### Your current environment ### Environment details gathered locally ```text vLLM server version: 0.19.0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Qwen3.5-9B-AWQ on ROCm/vLLM 0.19.0 can get stuck generating endless "!" inside JSON schema output bug;rocm ### Your current environment ### Environment details gathered locally ```text vLLM server version: 0.19.0...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: he prompt text itself looks clean: no suspicious control characters One reproducible failing case is based on: - ASIN: `0544938097` - market: `.com` - title: `Little Blue Truck's Springtime: An Easter And Springtime Boo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ite: No such file or directory saturnix is member of video group Model: QuantTrio/Qwen3.5-9B-AWQ Served model name: qwen3.5:9b Docker image: vllm/vllm-openai-rocm:latest Server launch command: sudo docker run --rm --net...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#20](https://github.com/vllm-project/vllm/pull/20) | mentioned | 0.45 | Optimize data movement | (noble numbat)" kernel: linux saturnix-ab350m-pro4 6.17.0-20-generic #20~24.04.1-ubuntu smp preempt_dynamic thu mar 19 01:28:37 utc 2 x86_64 x86_64 x86_64 gnu/linux python: python… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
