# vllm-project/vllm#3947: [Misc] [CI]: Flaky test failure in `test_chatglm3_lora`

| 字段 | 值 |
| --- | --- |
| Issue | [#3947](https://github.com/vllm-project/vllm/issues/3947) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc] [CI]: Flaky test failure in `test_chatglm3_lora`

### Issue 正文摘录

* [main CI failed](https://buildkite.com/vllm/ci/builds/4362#018ec42c-e40a-4cbd-943a-e2e4b6e11f53) after https://github.com/vllm-project/vllm/pull/3837 was merged * tracking in an issue in case we need to ~~fix-forward/revert/or maybe the test is flaky~~ @youkaichao confirmed the test is flaky ``` def test_chatglm3_lora(chatglm3_lora_files): llm = vllm.LLM(MODEL_PATH, max_model_len=1024, enable_lora=True, max_loras=4, max_lora_rank=64, trust_remote_code=True) expected_lora_output = [ "SELECT count(*) FROM singer", "SELECT avg(age) , min(age) , max(age) FROM singer WHERE country = 'France'", # noqa: E501 "SELECT name , country , age FROM singer ORDER BY age", ] output1 = do_sample(llm, chatglm3_lora_files, lora_id=1) for i in range(len(expected_lora_output)): assert output1[i] == expected_lora_output[i] output2 = do_sample(llm, chatglm3_lora_files, lora_id=2) for i in range(len(expected_lora_output)): > assert output2[i] == expected_lora_output[i] E AssertionError: assert '' == 'SELECT count(*) FROM singer' E E - SELECT count(*) FROM singer ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Misc] [CI]: Flaky test failure in `test_chatglm3_lora` * [main CI failed](https://buildkite.com/vllm/ci/builds/4362#018ec42c-e40a-4cbd-943a-e2e4b6e11f53) after https://github.com/vllm-project/vllm/pull/3837 was merged...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: def test_chatglm3_lora(chatglm3_lora_files): llm = vllm.LLM(MODEL_PATH, max_model_len=1024, enable_lora=True, max_loras=4, max_lora_rank=64, trust_remote_code=True)
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Misc] [CI]: Flaky test failure in `test_chatglm3_lora` * [main CI failed](https://buildkite.com/vllm/ci/builds/4362#018ec42c-e40a-4cbd-943a-e2e4b6e11f53) after https://github.com/vllm-project/vllm/pull/3837 was merged...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
