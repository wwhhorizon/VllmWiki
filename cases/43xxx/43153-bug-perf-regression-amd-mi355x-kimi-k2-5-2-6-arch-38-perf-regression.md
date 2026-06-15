# vllm-project/vllm#43153: [Bug][Perf Regression]: AMD MI355X Kimi K2.5/2.6 arch 38% perf regression

| 字段 | 值 |
| --- | --- |
| Issue | [#43153](https://github.com/vllm-project/vllm/issues/43153) |
| 状态 | open |
| 标签 | bug;rocm |
| 评论 | 24; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | hardware_porting;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | quantization |
| 症状 | slowdown |
| 根因提示 | dtype |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][Perf Regression]: AMD MI355X Kimi K2.5/2.6 arch 38% perf regression

### Issue 正文摘录

### Your current environment 0.21 ### 🐛 Describe the bug ### Human hi @hongxiayang +viz @powderluv @chunfangamd @andyluo7 kimi k2.5 int4 is regressing on mi355 a lot, can u take a look? thanks Live: https://inferencex.semianalysis.com/inference?g_model=Kimi-K2.5&g_rundate=2026-05-18&g_runid=26067557908&i_prec=int4&i_gpus=mi355x_vllm&i_dstart=2026-03-27&i_dend=2026-05-17&i_dates=2026-03-27&i_linelabel=1 ### AI Summary We're observing a large throughput regression for **Kimi K2.5 (INT4)** on **AMD MI355X** between vLLM ROCm **v0.18.0** and **v0.21.0**. | Date | vLLM ROCm | Token Throughput / GPU @ ~17 tok/s/user | InferenceX run | |---|---|---|---| | 2026-03-27 | **v0.18.0** | **~1,223 tok/s/gpu** (peak ~1,300) | [Actions run 23626527425](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/23626527425/attempts/1) · [config 23669977901](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/23669977901) | | 2026-05-17 | **v0.21.0** | **~753 tok/s/gpu** | [Actions run 25956503845](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/25956503845/attempts/1) · [config 25984517560](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/25984517560) | **Net regression: ~−...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug][Perf Regression]: AMD MI355X Kimi K2.5/2.6 arch 38% perf regression bug;rocm ### Your current environment 0.21 ### 🐛 Describe the bug ### Human hi @hongxiayang +viz @powderluv @chunfangamd @andyluo7 kimi k2.5 int4...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: uman hi @hongxiayang +viz @powderluv @chunfangamd @andyluo7 kimi k2.5 int4 is regressing on mi355 a lot, can u take a look? thanks Live: https://inferencex.semianalysis.com/inference?g_model=Kimi-K2.5&g_rundate=2026-05-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug][Perf Regression]: AMD MI355X Kimi K2.5/2.6 arch 38% perf regression bug;rocm ### Your current environment 0.21 ### 🐛 Describe the bug ### Human hi @hongxiayang +viz @powderluv @chunfangamd @andyluo7 kimi k2.5 int4...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ke a look? thanks Live: https://inferencex.semianalysis.com/inference?g_model=Kimi-K2.5&g_rundate=2026-05-18&g_runid=26067557908&i_prec=int4&i_gpus=mi355x_vllm&i_dstart=2026-03-27&i_dend=2026-05-17&i_dates=2026-03-27&i_...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ### Configuration | Field | Value | |---|---| | Model | Kimi K2.5 | | Precision | INT4 | | Hardware | MI355X | | Engine | vLLM (ROCm) | | ISL / OSL | 8K / 1K | | Source | SemiAnalysis InferenceX™ | Full SemiAnalysis Inf...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
