# vllm-project/vllm#34891: [Bug]: RuntimeError: [SymmDeviceMemory] Device does not support multicasting.

| 字段 | 值 |
| --- | --- |
| Issue | [#34891](https://github.com/vllm-project/vllm/issues/34891) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: [SymmDeviceMemory] Device does not support multicasting.

### Issue 正文摘录

### Trying to load Qwen3.5-397B-A17B-FP8 causes "RuntimeError: [SymmDeviceMemory] Device does not support multicasting" on 4xH200 GPUs Startparams: "--trust_remote_code", "--enable-auto-tool-choice", "--tool-call-parser", "qwen3_coder", "--reasoning-parser", "qwen3", "--limit_mm_per_prompt.image", "4", "--limit_mm_per_prompt.video", "0" ,"--tensor-parallel-size", "4" Full log: [qwen3.5_full_log.txt](https://github.com/user-attachments/files/25416025/qwen3.5_full_log.txt) I tried different nightly versions: [nightly-2b84ac669cfd8a4b6433b4ae4505028d9082c3a7](https://hub.docker.com/layers/vllm/vllm-openai/nightly-2b84ac669cfd8a4b6433b4ae4505028d9082c3a7/images/sha256-2f03b883d081cfa13ba86ecb3c0e25eac1802333d632a8f270ec3f0bca8e3ea8) [qwen3_5](https://hub.docker.com/layers/vllm/vllm-openai/qwen3_5/images/sha256-129644d37350c6f33cff8194344186a116de9784337e9ea30b2c5de03a093feb) [cu130-nightly-b6101d384db5709b4422ebd05fe84f0891ff63ce](https://hub.docker.com/layers/vllm/vllm-openai/cu130-nightly-b6101d384db5709b4422ebd05fe84f0891ff63ce/images/sha256-835f609594c17eaf8dfb7babf4cf3212a40aa301a813b7db7574728be60b53ef) [nightly-b6101d384db5709b4422ebd05fe84f0891ff63ce](https://hub.docker.com/la...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: achments/files/25416025/qwen3.5_full_log.txt) I tried different nightly versions: [nightly-2b84ac669cfd8a4b6433b4ae4505028d9082c3a7](https://hub.docker.com/layers/vllm/vllm-openai/nightly-2b84ac669cfd8a4b6433b4ae4505028...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: does not support multicasting. bug ### Trying to load Qwen3.5-397B-A17B-FP8 causes "RuntimeError: [SymmDeviceMemory] Device does not support multicasting" on 4xH200 GPUs Startparams: "--trust_remote_code", "--enable-aut...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: viceMemory] Device does not support multicasting. bug ### Trying to load Qwen3.5-397B-A17B-FP8 causes "RuntimeError: [SymmDeviceMemory] Device does not support multicasting" on 4xH200 GPUs Startparams: "--trust_remote_c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
