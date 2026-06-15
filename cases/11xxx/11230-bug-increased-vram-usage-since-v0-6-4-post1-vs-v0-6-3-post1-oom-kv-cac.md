# vllm-project/vllm#11230: [Bug]: Increased VRAM usage since v0.6.4.post1 (vs v0.6.3.post1) [OOM][KV cache]

| 字段 | 值 |
| --- | --- |
| Issue | [#11230](https://github.com/vllm-project/vllm/issues/11230) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Increased VRAM usage since v0.6.4.post1 (vs v0.6.3.post1) [OOM][KV cache]

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hello, I have a hard time understanding why the newer release make the hardware almost useless with such abysmal context size, if it wasn't for the older version i'd consider giving up. So just in case it's a bug and not a feature, i tried to show the most informations i can in this comparaison. If needed i can test anything else. Thanks # Hardware - GPU : NVIDIA A40-48Q - VRAM : 48GB - CUDA Version : 12.2 - Driver Version : 535.161.08 - OS : ```sh NAME="Red Hat Enterprise Linux" VERSION="8.10 (Ootpa)" ID="rhel" ID_LIKE="fedora" VERSION_ID="8.10" PLATFORM_ID="platform:el8" PRETTY_NAME="Red Hat Enterprise Linux 8.10 (Ootpa)" ANSI_COLOR="0;31" CPE_NAME="cpe:/o:redhat:enterprise_linux:8::baseos" HOME_URL="https://www.redhat.com/" DOCUMENTATION_URL="https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8" BUG_REPORT_URL="https://issues.redhat.com/" REDHAT_BUGZILLA_PRODUCT="Red Hat Enterprise Linux 8" REDHAT_BUGZILLA_PRODUCT_VERSION=8.10 REDHAT_SUPPORT_PRODUCT="Red Hat Enterprise Linux" REDHAT_SUPPORT_PRODUCT_VERSION="8.10" ``` # Test 1 ## Test 1.1 : Version v0.6.3.post1 - model : Q...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: lmost useless with such abysmal context size, if it wasn't for the older version i'd consider giving up. So just in case it's a bug and not a feature, i tried to show the most informations i can in this comparaison. If...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: .3.post1) [OOM][KV cache] bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hello, I have a hard time understanding why the newer release make the hardware almost useless...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: Test 1.1 : Version v0.6.3.post1 - model : Qwen-Qwen2.5-72B-Instruct-GPTQ-Int4 - max-model-len : 8192 - gpu-memory-utilization : 0.95 - enforce-eager : true - vram usage : 43787MiB / 49152MiB ## Test 1.2 : Version v0.6.3...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ding why the newer release make the hardware almost useless with such abysmal context size, if it wasn't for the older version i'd consider giving up. So just in case it's a bug and not a feature, i tried to show the mo...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: Increased VRAM usage since v0.6.4.post1 (vs v0.6.3.post1) [OOM][KV cache] bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hello, I have a hard time understanding...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
