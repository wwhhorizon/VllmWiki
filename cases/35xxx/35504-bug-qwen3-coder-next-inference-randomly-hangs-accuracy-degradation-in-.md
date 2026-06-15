# vllm-project/vllm#35504: [Bug]: qwen3-coder-next inference randomly hangs, accuracy degradation in 0.16.0+ with TP > 1 and  fuse_allreduce_rms=False (H100s on PCIe)

| 字段 | 值 |
| --- | --- |
| Issue | [#35504](https://github.com/vllm-project/vllm/issues/35504) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: qwen3-coder-next inference randomly hangs, accuracy degradation in 0.16.0+ with TP > 1 and  fuse_allreduce_rms=False (H100s on PCIe)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Symptoms: - model is unable to call tools properly e.g. fails to recall exact paths or identifiers from contexts of any length - is generally "lobotomized" - enters loops, misspells words, achieves lower scores on internal evals - inference randomly hangs, generating at full speed (at least according to logs and metrics) but never returning anything (The inference hanging might be a separate issue, #35502 possibly related) Running `qwen3-coder-next` with flags: ```bash - --model=Qwen/Qwen3-Coder-Next-FP8 - --served-model-name=qwen3-coder-latest - --max-model-len=131072 - --disable-log-requests - --tensor-parallel-size=2 - --no-enable-expert-parallel - --max-num-batched-tokens=32768 - --max-num-seqs=16 - --enable-auto-tool-choice - --tool-call-parser=qwen3_coder - --no-enable-prefix-caching ``` and envs: ```bash VLLM_USE_DEEP_GEMM=0 ``` **Notes / observations so far:** - tp=2, tp=4 - same behavior - FP8, BF16 - same behavior - same behavior on older versions (before #35085 ) with `-cc.pass_config.fuse_allreduce_rms=False` While getting the model to start is certainly an improvement, simply disabling allreduce fusion when symmmem i...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: radation in 0.16.0+ with TP > 1 and fuse_allreduce_rms=False (H100s on PCIe) bug ### Your current environment ### 🐛 Describe the bug Symptoms: - model is unable to call tools properly e.g. fails to recall exact paths or...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: n3-coder-next` with flags: ```bash - --model=Qwen/Qwen3-Coder-Next-FP8 - --served-model-name=qwen3-coder-latest - --max-model-len=131072 - --disable-log-requests - --tensor-parallel-size=2 - --no-enable-expert-parallel...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: curacy degradation in 0.16.0+ with TP > 1 and fuse_allreduce_rms=False (H100s on PCIe) bug ### Your current environment ### 🐛 Describe the bug Symptoms: - model is unable to call tools properly e.g. fails to recall exac...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: qwen3-coder-next inference randomly hangs, accuracy degradation in 0.16.0+ with TP > 1 and fuse_allreduce_rms=False (H100s on PCIe) bug ### Your current environment ### 🐛 Describe the bug Symptoms: - model is una...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: --disable-log-requests - --tensor-parallel-size=2 - --no-enable-expert-parallel - --max-num-batched-tokens=32768 - --max-num-seqs=16 - --enable-auto-tool-choice - --tool-call-parser=qwen3_coder - --no-enable-prefix-cach...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
