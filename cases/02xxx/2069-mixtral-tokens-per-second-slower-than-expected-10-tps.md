# vllm-project/vllm#2069: Mixtral tokens-per-second slower than expected, 10 tps

| 字段 | 值 |
| --- | --- |
| Issue | [#2069](https://github.com/vllm-project/vllm/issues/2069) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Mixtral tokens-per-second slower than expected, 10 tps

### Issue 正文摘录

I'm observing slower TPS than expected with mixtral. Specifically, I'm seeing ~10-11 TPS. It would be helpful to know what others have observed! ### Here's some details about my configuration: I've experimented with TP=2 and TP=4 with A100 80GBs. I'm running in a container with the following vllm and megablocks versions. ``` vllm @ git+https://github.com/vllm-project/vllm@d537c625cb039983a0bf61aa36ba8139a2905609 megablocks==0.5.0 ``` ### nvidia-smi ``` Tue Dec 12 22:19:27 2023 +---------------------------------------------------------------------------------------+ | NVIDIA-SMI 545.23.08 Driver Version: 545.23.08 CUDA Version: 12.3 | |-----------------------------------------+----------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+======================+======================| | 0 NVIDIA A100-SXM4-80GB Off | 00000000:00:05.0 Off | 0 | | N/A 36C P0 72W / 400W | 2MiB / 81920MiB | 0% Default | | | | Disabled | +-----------------------------------------+----------------------+----------------------+ | 1...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ps performance I'm observing slower TPS than expected with mixtral. Specifically, I'm seeing ~10-11 TPS. It would be helpful to know what others have observed! ### Here's some details about my configuration: I've experi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ful to know what others have observed! ### Here's some details about my configuration: I've experimented with TP=2 and TP=4 with A100 80GBs. I'm running in a container with the following vllm and megablocks versions. ``...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: tails about my configuration: I've experimented with TP=2 and TP=4 with A100 80GBs. I'm running in a container with the following vllm and megablocks versions. ``` vllm @ git+https://github.com/vllm-project/vllm@d537c62...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ==1.12 tokenizers==0.15.0 torch==2.1.1 tqdm==4.66.1 transformers==4.36.0 triton==2.1.0 typing_extensions==4.9.0 tzdata==2023.3 urllib3==2.1.0 uvicorn==0.24.0.post1 uvloop==0.19.0 vllm @ git+https://github.com/vllm-proje...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: on-dateutil==2.8.2 python-dotenv==1.0.0 pytz==2023.3.post1 PyYAML==6.0.1 quantile-python==1.1 ray==2.8.1 referencing==0.32.0 regex==2023.10.3 requests==2.31.0 rpds-py==0.13.2 safetensors==0.4.1 sentencepiece==0.1.99 six...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
